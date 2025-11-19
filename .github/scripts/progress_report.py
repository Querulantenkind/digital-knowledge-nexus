#!/usr/bin/env python3
"""
Generate progress report for repository.

Creates:
- Domain completion percentage
- Category status summary
- Recent activity
- Top contributors (if git available)
"""

import re
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def is_empty_file(filepath: Path) -> bool:
    """Check if file is empty template."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            return 'Add resources below' in content or '{Topic Name}' in content
    except:
        return True


def count_entries(filepath: Path) -> int:
    """Count entries in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Count ### headings (entries)
            return len(re.findall(r'^### ', content, re.MULTILINE))
    except:
        return 0


def analyze_category(category_path: Path) -> dict:
    """Analyze a single category."""
    format_files = ['books.md', 'papers.md', 'courses.md', 'videos.md',
                   'interactive.md', 'documentation.md', 'tools.md', 'podcasts-blogs.md']
    
    status = {
        'path': category_path,
        'name': category_path.name,
        'filled_files': 0,
        'empty_files': 0,
        'total_entries': 0,
    }
    
    for fmt in format_files:
        file_path = category_path / fmt
        if file_path.exists():
            if is_empty_file(file_path):
                status['empty_files'] += 1
            else:
                status['filled_files'] += 1
                status['total_entries'] += count_entries(file_path)
    
    status['completion'] = (status['filled_files'] / 8.0) * 100 if status['filled_files'] > 0 else 0
    
    return status


def find_categories(root: Path) -> list[dict]:
    """Find all categories and their status."""
    categories = []
    
    for domain_dir in sorted(root.iterdir()):
        if not domain_dir.is_dir() or not domain_dir.name[0].isdigit():
            continue
        
        # Find all leaf directories
        for path in domain_dir.rglob('*'):
            if path.is_dir():
                # Check if it has .md files
                if any(f.suffix == '.md' for f in path.iterdir() if f.is_file()):
                    # Check if it's a leaf (no subdirectories)
                    if not any(d.is_dir() and not d.name.startswith('.') for d in path.iterdir()):
                        status = analyze_category(path)
                        categories.append(status)
    
    return categories


def generate_report(root: Path):
    """Generate progress report."""
    print("="*80)
    print("DIGITAL KNOWLEDGE NEXUS - PROGRESS REPORT")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    print()
    
    categories = find_categories(root)
    
    # Overall stats
    total_categories = len(categories)
    completed = [c for c in categories if c['filled_files'] == 8]
    in_progress = [c for c in categories if 0 < c['filled_files'] < 8]
    not_started = [c for c in categories if c['filled_files'] == 0]
    
    total_entries = sum(c['total_entries'] for c in categories)
    
    print("📊 OVERALL PROGRESS")
    print(f"  Total categories: {total_categories}")
    print(f"  ✅ Completed: {len(completed)} ({len(completed)*100//total_categories}%)")
    print(f"  🔄 In progress: {len(in_progress)} ({len(in_progress)*100//total_categories}%)")
    print(f"  ⭕ Not started: {len(not_started)} ({len(not_started)*100//total_categories}%)")
    print(f"  📝 Total entries: {total_entries}")
    print()
    
    # Completed categories
    if completed:
        print("✅ COMPLETED CATEGORIES")
        for cat in sorted(completed, key=lambda x: x['total_entries'], reverse=True):
            rel_path = str(cat['path']).replace(str(root) + '/', '')
            print(f"  • {rel_path}")
            print(f"    └─ {cat['total_entries']} entries")
        print()
    
    # In progress categories
    if in_progress:
        print(f"🔄 IN PROGRESS ({len(in_progress)} categories)")
        for cat in sorted(in_progress, key=lambda x: x['completion'], reverse=True):
            rel_path = str(cat['path']).replace(str(root) + '/', '')
            print(f"  • {rel_path}")
            print(f"    └─ {cat['filled_files']}/8 files ({cat['completion']:.0f}%), {cat['total_entries']} entries")
        print()
    
    # Domain breakdown
    print("🌐 PROGRESS BY DOMAIN")
    domains = defaultdict(lambda: {'total': 0, 'completed': 0, 'in_progress': 0, 'entries': 0})
    
    for cat in categories:
        domain = str(cat['path']).split('/')[0]
        domains[domain]['total'] += 1
        domains[domain]['entries'] += cat['total_entries']
        if cat['filled_files'] == 8:
            domains[domain]['completed'] += 1
        elif cat['filled_files'] > 0:
            domains[domain]['in_progress'] += 1
    
    for domain in sorted(domains.keys()):
        d = domains[domain]
        pct = (d['completed'] * 100 // d['total']) if d['total'] > 0 else 0
        print(f"  {domain:40s}: {d['completed']:3d}/{d['total']:3d} completed ({pct:3d}%), {d['entries']:4d} entries")
    print()
    
    # Top categories by content
    print("🏆 TOP CATEGORIES BY CONTENT")
    top = sorted([c for c in categories if c['total_entries'] > 0], 
                 key=lambda x: x['total_entries'], reverse=True)[:10]
    
    for i, cat in enumerate(top, 1):
        rel_path = str(cat['path']).replace(str(root) + '/', '')
        print(f"  {i:2d}. {cat['total_entries']:3d} entries - {rel_path}")
    print()
    
    # Suggestions
    print("💡 SUGGESTIONS")
    if in_progress:
        print("  Priority: Complete in-progress categories")
        for cat in sorted(in_progress, key=lambda x: x['completion'], reverse=True)[:3]:
            rel_path = str(cat['path']).replace(str(root) + '/', '')
            remaining = 8 - cat['filled_files']
            print(f"  • {rel_path} (only {remaining} file{'s' if remaining > 1 else ''} remaining)")
    else:
        print("  Start with high-impact categories in AI, Software Engineering, or Fundamentals")
    print()


def main():
    """Main function."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    generate_report(repo_root)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
