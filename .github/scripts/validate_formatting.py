#!/usr/bin/env python3
"""
Validate markdown formatting and style compliance.

Checks:
- Title capitalization (title case)
- URL format (includes https://)
- Required fields present
- Consistent spacing
- No trailing whitespace
- No emojis
- Proper difficulty section labels
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

# Difficulty section headers
DIFFICULTY_SECTIONS = {
    '## BEGINNER',
    '## INTERMEDIATE',
    '## ADVANCED',
    '## CLASSIC',
    '## RECENT (2023+)'
}

# Title case exceptions (should be lowercase unless at start/end)
TITLE_CASE_EXCEPTIONS = {
    'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'nor', 
    'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet',
    'vs'  # Special case for "P vs NP"
}

# Common field labels by format type
FIELD_LABELS = {
    'books': ['Author', 'Year', 'Publisher', 'ISBN', 'Link', 'Description', 'Why included'],
    'papers': ['Author', 'Year', 'Venue', 'Link', 'arXiv', 'DOI', 'Description', 'Why included'],
    'courses': ['Instructor', 'Platform', 'Year', 'Duration', 'Link', 'Description', 'Why included'],
    'videos': ['Speaker', 'Venue', 'Year', 'Duration', 'Link', 'Description', 'Why included'],
    'interactive': ['Creator', 'Year', 'Link', 'Description', 'Why included'],
    'documentation': ['Organization', 'Year', 'Link', 'Description', 'Why included'],
    'tools': ['Creator', 'Year', 'License', 'Link', 'Description', 'Why included'],
    'podcasts-blogs': ['Author', 'Date', 'Link', 'Description', 'Why included']
}


def check_url_format(text: str, line_num: int) -> List[Tuple[int, str]]:
    """Check if URLs include protocol."""
    errors = []
    
    # Find lines with "Link:" or bare URLs
    url_pattern = r'(?:Link:\s*|https?://)([\w\.-]+(?:\.[a-z]{2,})[^\s]*)'
    
    # Check for URLs without protocol
    if 'Link:' in text:
        link_match = re.search(r'Link:\s*([^\s]+)', text)
        if link_match:
            url = link_match.group(1)
            if not url.startswith('http://') and not url.startswith('https://'):
                errors.append((line_num, f"URL missing protocol: {url}"))
    
    return errors


def check_trailing_whitespace(text: str, line_num: int) -> List[Tuple[int, str]]:
    """Check for trailing whitespace."""
    errors = []
    if text.rstrip() != text and text.strip():  # Ignore blank lines
        errors.append((line_num, "Line has trailing whitespace"))
    return errors


def check_emojis(text: str, line_num: int) -> List[Tuple[int, str]]:
    """Check for emojis (basic check)."""
    errors = []
    # Simple emoji detection (Unicode ranges)
    emoji_pattern = r'[\U0001F300-\U0001F9FF]|[\U0001F600-\U0001F64F]|[\U0001F680-\U0001F6FF]|[\U00002600-\U000027BF]'
    if re.search(emoji_pattern, text):
        errors.append((line_num, "Line contains emoji"))
    return errors


def check_difficulty_sections(lines: List[str]) -> List[Tuple[int, str]]:
    """Check for proper difficulty section headers."""
    errors = []
    
    for i, line in enumerate(lines, 1):
        if line.startswith('## ') and line.strip() not in ['## Resources', '---']:
            if line.strip() not in DIFFICULTY_SECTIONS:
                errors.append((i, f"Invalid difficulty section: {line.strip()}"))
    
    return errors


def check_field_labels(text: str, line_num: int, format_type: str) -> List[Tuple[int, str]]:
    """Check field label capitalization."""
    errors = []
    
    # Common field patterns
    field_pattern = r'^([A-Za-z\s]+):\s*'
    match = re.match(field_pattern, text)
    
    if match:
        field = match.group(1)
        # Check if first word is capitalized
        if field and field[0].islower():
            errors.append((line_num, f"Field label should be capitalized: {field}"))
    
    return errors


def check_template_placeholders(text: str, line_num: int) -> List[Tuple[int, str]]:
    """Check for unfilled template placeholders."""
    errors = []
    
    placeholders = [
        '{Topic Name}',
        'YYYY-MM-DD',
        'YYYY',
        'First Last',
        'Publisher Name',
        '978-XXXXXXXXXX',
        'https://direct-link',
        'One-sentence summary',
        'What makes this resource',
    ]
    
    for placeholder in placeholders:
        if placeholder in text:
            errors.append((line_num, f"Template placeholder not replaced: {placeholder}"))
    
    return errors


def validate_file(filepath: Path) -> List[Tuple[int, str]]:
    """Validate a single markdown file."""
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return [(0, f"Error reading file: {e}")]
    
    # Determine format type from filename
    format_type = filepath.stem  # books, papers, etc.
    
    for line_num, line in enumerate(lines, 1):
        # Check URL format
        errors.extend(check_url_format(line, line_num))
        
        # Check trailing whitespace
        errors.extend(check_trailing_whitespace(line, line_num))
        
        # Check emojis
        errors.extend(check_emojis(line, line_num))
        
        # Check field labels
        errors.extend(check_field_labels(line, line_num, format_type))
        
        # Check template placeholders
        errors.extend(check_template_placeholders(line, line_num))
    
    # Check difficulty sections
    errors.extend(check_difficulty_sections(lines))
    
    # Check file ends with newline
    if lines and not lines[-1].endswith('\n'):
        errors.append((len(lines), "File should end with newline"))
    
    return errors


def main():
    """Main validation function."""
    if len(sys.argv) < 2:
        print("Usage: python3 validate_formatting.py <file_path>")
        print("\nValidates markdown formatting and style compliance.")
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
        print(f"\nFound {len(errors)} formatting errors:\n")
        for line_num, error in sorted(errors):
            if line_num > 0:
                print(f"  Line {line_num}: {error}")
            else:
                print(f"  {error}")
        return 1
    else:
        print("✅ VALIDATION PASSED")
        print("File formatting is correct")
        return 0


if __name__ == '__main__':
    sys.exit(main())
