#!/usr/bin/env python3
"""
Validate content quality and completeness.

Checks:
- Years are reasonable (1950-2026)
- Descriptions are non-empty
- No duplicate entries in same file
- Required fields are present
- ISBN format is valid
- DOI format is valid
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Set

CURRENT_YEAR = 2025


def extract_entries(lines: List[str]) -> List[Dict]:
    """Extract entries from markdown file."""
    entries = []
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
                'fields': {}
            }
        
        # Field line (e.g., "Author: Name")
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


def check_year_validity(year_str: str) -> bool:
    """Check if year is reasonable."""
    try:
        # Handle ranges like "2020-2024"
        if '-' in year_str and year_str != 'YYYY-MM-DD':
            years = year_str.split('-')
            for y in years:
                y = y.strip()
                if y == 'Present':
                    continue
                year = int(y)
                if year < 1950 or year > CURRENT_YEAR + 1:
                    return False
            return True
        
        # Handle single year
        year_match = re.search(r'\d{4}', year_str)
        if year_match:
            year = int(year_match.group())
            return 1950 <= year <= CURRENT_YEAR + 1
        
        # Special cases
        if 'Living Document' in year_str or 'Present' in year_str:
            return True
        
        return False
    except:
        return False


def check_isbn_format(isbn: str) -> bool:
    """Check if ISBN format is valid."""
    # Remove hyphens and spaces
    isbn_clean = isbn.replace('-', '').replace(' ', '')
    
    # ISBN-13 should be 13 digits starting with 978 or 979
    if len(isbn_clean) == 13 and isbn_clean.isdigit():
        return isbn_clean.startswith('978') or isbn_clean.startswith('979')
    
    # ISBN-10 should be 10 characters (9 digits + check digit which can be X)
    if len(isbn_clean) == 10:
        return isbn_clean[:9].isdigit() and (isbn_clean[9].isdigit() or isbn_clean[9] == 'X')
    
    return False


def check_doi_format(doi: str) -> bool:
    """Check if DOI format is valid."""
    # DOI format: 10.XXXX/...
    doi_pattern = r'^10\.\d{4,}/[^\s]+$'
    return bool(re.match(doi_pattern, doi))


def validate_entry(entry: Dict, format_type: str) -> List[str]:
    """Validate a single entry."""
    errors = []
    title = entry['title']
    fields = entry['fields']
    
    # Check for empty title
    if not title or title == 'Book Title: Subtitle if Present':
        errors.append(f"Empty or template title in {entry['section']}")
    
    # Check required fields based on format type
    required_fields = {
        'books': ['Author', 'Year', 'Publisher', 'Link', 'Description', 'Why included'],
        'papers': ['Author', 'Year', 'Link', 'Description', 'Why included'],
        'courses': ['Year', 'Link', 'Description', 'Why included'],
        'videos': ['Year', 'Link', 'Description', 'Why included'],
        'interactive': ['Year', 'Link', 'Description', 'Why included'],
        'documentation': ['Year', 'Link', 'Description', 'Why included'],
        'tools': ['Year', 'Link', 'Description', 'Why included'],
        'podcasts-blogs': ['Link', 'Description', 'Why included']
    }
    
    if format_type in required_fields:
        for field in required_fields[format_type]:
            if field not in fields or not fields[field]:
                errors.append(f"Missing required field '{field}' in entry: {title}")
    
    # Validate Year field
    if 'Year' in fields and fields['Year']:
        if not check_year_validity(fields['Year']):
            errors.append(f"Invalid year format in entry '{title}': {fields['Year']}")
    
    # Validate ISBN
    if 'ISBN' in fields and fields['ISBN']:
        isbn = fields['ISBN']
        if isbn != '978-XXXXXXXXXX' and not check_isbn_format(isbn):
            errors.append(f"Invalid ISBN format in entry '{title}': {isbn}")
    
    # Validate DOI
    if 'DOI' in fields and fields['DOI']:
        doi = fields['DOI']
        if not check_doi_format(doi):
            errors.append(f"Invalid DOI format in entry '{title}': {doi}")
    
    # Check for empty description
    if 'Description' in fields:
        desc = fields['Description']
        if not desc or len(desc) < 10 or desc == 'One-sentence summary of scope and content':
            errors.append(f"Empty or template description in entry: {title}")
    
    # Check for empty "Why included"
    if 'Why included' in fields:
        why = fields['Why included']
        if not why or len(why) < 10 or why == 'What makes this resource valuable or unique':
            errors.append(f"Empty or template 'Why included' in entry: {title}")
    
    return errors


def check_duplicates(entries: List[Dict]) -> List[str]:
    """Check for duplicate entries."""
    errors = []
    
    seen_titles: Set[str] = set()
    seen_links: Set[str] = set()
    
    for entry in entries:
        title = entry['title'].lower()
        
        # Check duplicate titles
        if title in seen_titles:
            errors.append(f"Duplicate title found: {entry['title']}")
        seen_titles.add(title)
        
        # Check duplicate links
        if 'Link' in entry['fields']:
            link = entry['fields']['Link'].lower()
            if link and link != 'https://direct-link-to-book.com':
                if link in seen_links:
                    errors.append(f"Duplicate link found in entry: {entry['title']}")
                seen_links.add(link)
    
    return errors


def validate_file(filepath: Path) -> List[str]:
    """Validate a single markdown file."""
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return [f"Error reading file: {e}"]
    
    # Determine format type from filename
    format_type = filepath.stem  # books, papers, etc.
    
    # Extract entries
    entries = extract_entries([line.rstrip() for line in lines])
    
    if not entries:
        # Check if file has template marker (acceptable for empty files)
        content = ''.join(lines)
        if 'Add resources below' in content or '{Topic Name}' in content:
            return []  # Empty template file is OK
        errors.append("No entries found in file")
        return errors
    
    # Validate each entry
    for entry in entries:
        entry_errors = validate_entry(entry, format_type)
        errors.extend(entry_errors)
    
    # Check for duplicates
    duplicate_errors = check_duplicates(entries)
    errors.extend(duplicate_errors)
    
    return errors


def main():
    """Main validation function."""
    if len(sys.argv) < 2:
        print("Usage: python3 validate_content.py <file_path>")
        print("\nValidates content quality and completeness.")
        return 1
    
    filepath = Path(sys.argv[1])
    
    if not filepath.exists():
        print(f"❌ Error: File not found: {filepath}")
        return 1
    
    if not filepath.suffix == '.md':
        print(f"❌ Error: Not a markdown file: {filepath}")
        return 1
    
    print(f"Validating: {filepath}")
    print()
    
    errors = validate_file(filepath)
    
    if errors:
        print(f"❌ VALIDATION FAILED")
        print(f"\nFound {len(errors)} content errors:\n")
        for error in errors:
            print(f"  • {error}")
        return 1
    else:
        print("✅ VALIDATION PASSED")
        print("Content validation successful")
        return 0


if __name__ == '__main__':
    sys.exit(main())
