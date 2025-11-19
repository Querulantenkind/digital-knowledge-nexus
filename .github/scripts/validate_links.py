#!/usr/bin/env python3
"""
Check all URLs for accessibility.

Checks HTTP status codes and warns about broken links.
"""

import re
import sys
import time
import argparse
from pathlib import Path
from typing import List, Tuple, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    print("Error: requests library not installed")
    print("Install with: pip install requests")
    sys.exit(1)


def extract_urls(filepath: Path) -> List[Tuple[int, str]]:
    """Extract all URLs from a markdown file."""
    urls = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    for line_num, line in enumerate(lines, 1):
        # Find URLs in Link: fields
        link_match = re.search(r'Link:\s*(https?://[^\s]+)', line)
        if link_match:
            urls.append((line_num, link_match.group(1)))
        
        # Find DOI URLs
        doi_match = re.search(r'DOI:\s*(10\.\d{4,}/[^\s]+)', line)
        if doi_match:
            doi_url = f"https://doi.org/{doi_match.group(1)}"
            urls.append((line_num, doi_url))
        
        # Find arXiv URLs
        arxiv_match = re.search(r'arXiv:\s*(\d{4}\.\d{4,})', line)
        if arxiv_match:
            arxiv_url = f"https://arxiv.org/abs/{arxiv_match.group(1)}"
            urls.append((line_num, arxiv_url))
    
    return urls


def check_url(url: str, timeout: int = 10) -> Dict:
    """Check if a URL is accessible."""
    result = {
        'url': url,
        'status': None,
        'error': None,
        'redirect': None,
        'response_time': None
    }
    
    try:
        start_time = time.time()
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        result['response_time'] = time.time() - start_time
        result['status'] = response.status_code
        
        # Check for redirects
        if response.history:
            result['redirect'] = response.url
        
    except requests.exceptions.Timeout:
        result['error'] = 'Timeout'
    except requests.exceptions.ConnectionError:
        result['error'] = 'Connection Error'
    except requests.exceptions.TooManyRedirects:
        result['error'] = 'Too Many Redirects'
    except requests.exceptions.RequestException as e:
        result['error'] = str(e)
    except Exception as e:
        result['error'] = f"Unexpected error: {e}"
    
    return result


def validate_file(filepath: Path, timeout: int = 10, parallel: int = 5) -> List[Dict]:
    """Validate all URLs in a file."""
    print(f"Extracting URLs from {filepath}...")
    urls = extract_urls(filepath)
    
    if not urls:
        print("No URLs found in file")
        return []
    
    print(f"Found {len(urls)} URLs")
    print(f"Checking URLs (timeout: {timeout}s, parallel: {parallel})...\n")
    
    results = []
    
    with ThreadPoolExecutor(max_workers=parallel) as executor:
        # Submit all URL checks
        future_to_url = {
            executor.submit(check_url, url, timeout): (line_num, url)
            for line_num, url in urls
        }
        
        # Process results as they complete
        for i, future in enumerate(as_completed(future_to_url), 1):
            line_num, url = future_to_url[future]
            try:
                result = future.result()
                result['line_num'] = line_num
                results.append(result)
                
                # Progress indicator
                status_symbol = '✓' if result['status'] == 200 else '✗' if result['error'] else '⚠'
                print(f"[{i}/{len(urls)}] {status_symbol} {url[:80]}")
                
            except Exception as e:
                results.append({
                    'line_num': line_num,
                    'url': url,
                    'error': str(e)
                })
    
    return results


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Validate URLs in markdown files')
    parser.add_argument('file', type=str, help='Path to markdown file')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds')
    parser.add_argument('--parallel', type=int, default=5, help='Number of parallel requests')
    
    args = parser.parse_args()
    
    filepath = Path(args.file)
    
    if not filepath.exists():
        print(f"❌ Error: File not found: {filepath}")
        return 1
    
    results = validate_file(filepath, timeout=args.timeout, parallel=args.parallel)
    
    if not results:
        print("\n✅ No URLs to validate")
        return 0
    
    # Categorize results
    success = [r for r in results if r['status'] == 200]
    warnings = [r for r in results if r['status'] and r['status'] != 200 and not r['error']]
    errors = [r for r in results if r['error']]
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total URLs: {len(results)}")
    print(f"✓ Success (200 OK): {len(success)}")
    print(f"⚠ Warnings: {len(warnings)}")
    print(f"✗ Errors: {len(errors)}")
    
    # Print warnings
    if warnings:
        print("\n⚠ WARNINGS:")
        for r in warnings:
            print(f"  Line {r['line_num']}: HTTP {r['status']} - {r['url']}")
            if r['redirect']:
                print(f"    → Redirects to: {r['redirect']}")
    
    # Print errors
    if errors:
        print("\n✗ ERRORS:")
        for r in errors:
            print(f"  Line {r['line_num']}: {r['error']} - {r['url']}")
    
    # Check for slow responses
    slow_urls = [r for r in results if r.get('response_time') and r['response_time'] > 5]
    if slow_urls:
        print("\n⏱ SLOW RESPONSES (>5s):")
        for r in slow_urls:
            print(f"  Line {r['line_num']}: {r['response_time']:.2f}s - {r['url']}")
    
    # Return exit code
    if errors:
        print("\n❌ VALIDATION FAILED: Some URLs have errors")
        return 1
    elif warnings:
        print("\n⚠ VALIDATION PASSED WITH WARNINGS")
        return 0
    else:
        print("\n✅ VALIDATION PASSED: All URLs accessible")
        return 0


if __name__ == '__main__':
    sys.exit(main())
