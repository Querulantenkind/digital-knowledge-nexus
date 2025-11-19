#!/usr/bin/env python3
"""
Generate repository statistics.

Output:
- Total files and entries count
- Distribution by difficulty level
- Distribution by format type
- Distribution by year
- Coverage by domain
"""

import re
import sys
from pathlib import Path
from typing import Dict, List
from collections import defaultdict


def extract_entries_with_metadata(filepath: Path) -> List[Dict]:
    """Extract entries with metadata from markdown file."""
    entries = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return []
    
    current_entry = None
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        # Track difficulty sections
        if line.startswith('## ') and line in ['## BEGINNER', '## INTERMEDIATE', '## ADVANCED', '## CLASSIC', '## RECENT (2023+)']:
            current_section = line[3:].strip()
            continue
        
        # Entry starts with ###
        if line.startswith('### '):
            if current_entry:
                entries.append(current_entry)
            current_entry = {
                'title': line[4:].strip(),
                'section': current_section,
                'fields': {},
                'file': filepath
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
        entries.append(current_entry)
    
    return entries


def is_empty_file(filepath: Path) -> bool:
    """Check if file is empty (template only)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            return 'Add resources below' in content or '{Topic Name}' in content
    except:
        return True


def collect_statistics(root: Path) -> Dict:
    """Collect repository statistics."""
    stats = {
        'total_files': 0,
        'empty_files': 0,
        'filled_files': 0,
        'total_entries': 0,
        'by_format': defaultdict(int),
        'by_difficulty': defaultdict(int),
        'by_domain': defaultdict(int),
        'by_year': defaultdict(int),
        'entries_by_format': defaultdict(int),
    }
    
    # Iterate through all markdown files
    for md_file in root.rglob('*.md'):
        # Skip template and meta files
        if 'TEMPLATE' in str(md_file):
            continue
        
        # Get relative path parts
        try:
            rel_path = md_file.relative_to(root)
            if not str(rel_path.parts[0])[0].isdigit():
                continue
        except (ValueError, IndexError):
            continue
        
        stats['total_files'] += 1
        
        # Get format type
        format_type = md_file.stem
        stats['by_format'][format_type] += 1
        
        # Get domain from relative path
        try:
            rel_path = md_file.relative_to(root)
            domain = str(rel_path.parts[0])
            stats['by_domain'][domain] += 1
        except (ValueError, IndexError):
            pass
        
        # Check if empty
        if is_empty_file(md_file):
            stats['empty_files'] += 1
            continue
        
        stats['filled_files'] += 1
        
        # Extract entries
        entries = extract_entries_with_metadata(md_file)
        stats['total_entries'] += len(entries)
        stats['entries_by_format'][format_type] += len(entries)
        
        # Count by difficulty and year
        for entry in entries:
            if entry['section']:
                stats['by_difficulty'][entry['section']] += 1
            
            if 'Year' in entry['fields']:
                year_str = entry['fields']['Year']
                # Extract first 4-digit year
                year_match = re.search(r'(\d{4})', year_str)
                if year_match:
                    year = year_match.group(1)
                    decade = (int(year) // 10) * 10
                    stats['by_year'][f"{decade}s"] += 1
    
    return stats


def print_statistics(stats: Dict):
    """Print formatted statistics."""
    print("="*80)
    print("DIGITAL KNOWLEDGE NEXUS - REPOSITORY STATISTICS")
    print("="*80)
    print()
    
    # Overall stats
    print("📊 OVERALL")
    print(f"  Total format files: {stats['total_files']}")
    print(f"  Filled files: {stats['filled_files']}")
    print(f"  Empty templates: {stats['empty_files']}")
    print(f"  Total entries: {stats['total_entries']}")
    print(f"  Completion: {stats['filled_files']*100//stats['total_files']}%")
    print()
    
    # By format
    print("📚 BY FORMAT TYPE")
    format_order = ['books', 'papers', 'courses', 'videos', 'interactive', 'documentation', 'tools', 'podcasts-blogs']
    for fmt in format_order:
        if fmt in stats['by_format']:
            total = stats['by_format'][fmt]
            entries = stats['entries_by_format'][fmt]
            avg = entries / total if total > 0 else 0
            print(f"  {fmt:15s}: {total:4d} files, {entries:5d} entries (avg {avg:.1f} per file)")
    print()
    
    # By difficulty
    print("🎯 BY DIFFICULTY LEVEL")
    difficulty_order = ['BEGINNER', 'INTERMEDIATE', 'ADVANCED', 'CLASSIC', 'RECENT (2023+)']
    total_difficulty = sum(stats['by_difficulty'].values())
    for diff in difficulty_order:
        if diff in stats['by_difficulty']:
            count = stats['by_difficulty'][diff]
            pct = count * 100 / total_difficulty if total_difficulty > 0 else 0
            print(f"  {diff:20s}: {count:5d} entries ({pct:5.1f}%)")
    print()
    
    # By domain
    print("🌐 BY DOMAIN")
    for domain in sorted(stats['by_domain'].keys()):
        files = stats['by_domain'][domain]
        print(f"  {domain:40s}: {files:4d} files")
    print()
    
    # By year/decade
    print("📅 BY DECADE")
    for decade in sorted(stats['by_year'].keys(), reverse=True):
        count = stats['by_year'][decade]
        print(f"  {decade:10s}: {count:5d} entries")
    print()


def main():
    """Main function."""
    # Get repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    print("Collecting statistics...")
    print(f"Repository: {repo_root}")
    print()
    
    stats = collect_statistics(repo_root)
    
    print_statistics(stats)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
