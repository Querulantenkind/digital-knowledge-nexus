#!/usr/bin/env python3
"""
Find duplicate entries across files.

Checks for:
- Same title in multiple files
- Same URL in multiple entries
- Same ISBN/DOI in multiple entries
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


def extract_entry_data(filepath: Path) -> List[Dict]:
    """Extract entry data from markdown file."""
    entries = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return []
    
    current_entry = None
    
    for line in lines:
        line = line.strip()
        
        # Entry starts with ###
        if line.startswith('### '):
            if current_entry:
                current_entry['file'] = str(filepath)
                entries.append(current_entry)
            current_entry = {
                'title': line[4:].strip(),
                'fields': {}
            }
        
        # Field line
        elif current_entry and ':' in line:
            field_match = re.match(r'^([A-Za-z\s]+):\s*(.*)$', line)
            if field_match:
                field_name = field_match.group(1).strip()
                field_value = field_match.group(2).strip()
                current_entry['fields'][field_name] = field_value
    
    # Add last entry
    if current_entry:
        current_entry['file'] = str(filepath)
        entries.append(current_entry)
    
    return entries


def find_all_entries(directory: Path) -> List[Dict]:
    """Find all entries in all markdown files."""
    all_entries = []
    
    # Find all .md files in domain directories
    for md_file in directory.rglob('*.md'):
        # Skip template files and meta files
        if 'TEMPLATE' in str(md_file) or not str(md_file).split('/')[0][0].isdigit():
            continue
        
        entries = extract_entry_data(md_file)
        all_entries.extend(entries)
    
    return all_entries


def find_duplicate_titles(entries: List[Dict]) -> List[Tuple[str, List[str]]]:
    """Find duplicate titles across files."""
    title_to_files: Dict[str, List[str]] = defaultdict(list)
    
    for entry in entries:
        title = entry['title'].lower().strip()
        if title and title != 'book title: subtitle if present':
            title_to_files[title].append(entry['file'])
    
    # Find titles that appear in multiple files
    duplicates = []
    for title, files in title_to_files.items():
        if len(files) > 1:
            duplicates.append((title, list(set(files))))
    
    return duplicates


def find_duplicate_links(entries: List[Dict]) -> List[Tuple[str, List[str]]]:
    """Find duplicate links across files."""
    link_to_files: Dict[str, List[str]] = defaultdict(list)
    
    for entry in entries:
        if 'Link' in entry['fields']:
            link = entry['fields']['Link'].strip()
            if link and link not in ['https://direct-link-to-book.com', 'https://...']:
                link_to_files[link].append(entry['file'])
    
    # Find links that appear in multiple files
    duplicates = []
    for link, files in link_to_files.items():
        if len(files) > 1:
            duplicates.append((link, list(set(files))))
    
    return duplicates


def find_duplicate_isbns(entries: List[Dict]) -> List[Tuple[str, List[str]]]:
    """Find duplicate ISBNs across files."""
    isbn_to_files: Dict[str, List[str]] = defaultdict(list)
    
    for entry in entries:
        if 'ISBN' in entry['fields']:
            isbn = entry['fields']['ISBN'].strip()
            if isbn and isbn != '978-XXXXXXXXXX':
                isbn_to_files[isbn].append(entry['file'])
    
    # Find ISBNs that appear in multiple files
    duplicates = []
    for isbn, files in isbn_to_files.items():
        if len(files) > 1:
            duplicates.append((isbn, list(set(files))))
    
    return duplicates


def find_duplicate_dois(entries: List[Dict]) -> List[Tuple[str, List[str]]]:
    """Find duplicate DOIs across files."""
    doi_to_files: Dict[str, List[str]] = defaultdict(list)
    
    for entry in entries:
        if 'DOI' in entry['fields']:
            doi = entry['fields']['DOI'].strip()
            if doi and doi not in ['10.XXXX/...', '']:
                doi_to_files[doi].append(entry['file'])
    
    # Find DOIs that appear in multiple files
    duplicates = []
    for doi, files in doi_to_files.items():
        if len(files) > 1:
            duplicates.append((doi, list(set(files))))
    
    return duplicates


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python3 check_duplicates.py <directory>")
        print("\nFinds duplicate entries across all markdown files in directory.")
        return 1
    
    directory = Path(sys.argv[1])
    
    if not directory.exists():
        print(f"❌ Error: Directory not found: {directory}")
        return 1
    
    print(f"Scanning for duplicates in {directory}...")
    print()
    
    # Extract all entries
    entries = find_all_entries(directory)
    print(f"Found {len(entries)} total entries")
    print()
    
    # Find duplicates
    duplicate_titles = find_duplicate_titles(entries)
    duplicate_links = find_duplicate_links(entries)
    duplicate_isbns = find_duplicate_isbns(entries)
    duplicate_dois = find_duplicate_dois(entries)
    
    has_duplicates = False
    
    # Report duplicate titles
    if duplicate_titles:
        has_duplicates = True
        print(f"❌ DUPLICATE TITLES ({len(duplicate_titles)}):\n")
        for title, files in duplicate_titles:
            print(f"  Title: {title}")
            for f in sorted(files):
                print(f"    → {f}")
            print()
    
    # Report duplicate links
    if duplicate_links:
        has_duplicates = True
        print(f"❌ DUPLICATE LINKS ({len(duplicate_links)}):\n")
        for link, files in duplicate_links:
            print(f"  Link: {link}")
            for f in sorted(files):
                print(f"    → {f}")
            print()
    
    # Report duplicate ISBNs
    if duplicate_isbns:
        has_duplicates = True
        print(f"❌ DUPLICATE ISBNs ({len(duplicate_isbns)}):\n")
        for isbn, files in duplicate_isbns:
            print(f"  ISBN: {isbn}")
            for f in sorted(files):
                print(f"    → {f}")
            print()
    
    # Report duplicate DOIs
    if duplicate_dois:
        has_duplicates = True
        print(f"❌ DUPLICATE DOIs ({len(duplicate_dois)}):\n")
        for doi, files in duplicate_dois:
            print(f"  DOI: {doi}")
            for f in sorted(files):
                print(f"    → {f}")
            print()
    
    if not has_duplicates:
        print("✅ No duplicates found")
        return 0
    else:
        total_dupes = len(duplicate_titles) + len(duplicate_links) + len(duplicate_isbns) + len(duplicate_dois)
        print(f"Found {total_dupes} duplicate entries")
        return 1


if __name__ == '__main__':
    sys.exit(main())
