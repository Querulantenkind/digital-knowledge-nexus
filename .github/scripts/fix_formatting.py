#!/usr/bin/env python3
"""
Fix common formatting issues automatically.

Fixes:
- Trailing whitespace
- Missing final newline
- Inconsistent spacing between sections
"""

import sys
from pathlib import Path


def fix_trailing_whitespace(lines: list[str]) -> list[str]:
    """Remove trailing whitespace from all lines."""
    return [line.rstrip() + '\n' if line.strip() else '\n' for line in lines]


def ensure_final_newline(lines: list[str]) -> list[str]:
    """Ensure file ends with a newline."""
    if lines and not lines[-1].endswith('\n'):
        lines[-1] = lines[-1] + '\n'
    return lines


def normalize_section_spacing(lines: list[str]) -> list[str]:
    """Ensure consistent spacing between sections."""
    result = []
    prev_was_separator = False
    
    for line in lines:
        is_separator = line.strip() == '---'
        is_heading = line.strip().startswith('#')
        
        # Add blank line before separators and headings (except at start)
        if (is_separator or is_heading) and result and result[-1].strip():
            result.append('\n')
        
        result.append(line)
        prev_was_separator = is_separator
    
    return result


def fix_file(filepath: Path, dry_run: bool = False) -> tuple[bool, list[str]]:
    """Fix formatting issues in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    original_lines = lines.copy()
    changes = []
    
    # Apply fixes
    lines = fix_trailing_whitespace(lines)
    lines = ensure_final_newline(lines)
    lines = normalize_section_spacing(lines)
    
    # Check if changes were made
    if lines != original_lines:
        changes.append(f"Fixed {filepath}")
        
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        
        return True, changes
    
    return False, []


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Fix common formatting issues')
    parser.add_argument('files', nargs='+', help='Files to fix')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be fixed without making changes')
    
    args = parser.parse_args()
    
    total_fixed = 0
    
    for filepath in args.files:
        path = Path(filepath)
        if not path.exists():
            print(f"⚠️  File not found: {filepath}")
            continue
        
        modified, changes = fix_file(path, dry_run=args.dry_run)
        
        if modified:
            total_fixed += 1
            status = "Would fix" if args.dry_run else "✓ Fixed"
            print(f"{status}: {filepath}")
        else:
            print(f"  No changes needed: {filepath}")
    
    print(f"\n{'Would fix' if args.dry_run else 'Fixed'} {total_fixed} file(s)")
    
    return 0 if total_fixed == 0 else 0


if __name__ == '__main__':
    sys.exit(main())
