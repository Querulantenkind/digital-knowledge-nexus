#!/usr/bin/env python3
"""
Validate repository structure and file organization.

Checks:
- All category directories have exactly 8 format files
- File names match expected formats
- No unexpected files in category directories
"""

import os
import sys
from pathlib import Path

# Expected format files in each leaf directory
EXPECTED_FILES = {
    'books.md',
    'papers.md',
    'courses.md',
    'videos.md',
    'interactive.md',
    'documentation.md',
    'tools.md',
    'podcasts-blogs.md'
}

# Domain directories (01-12)
DOMAIN_PATTERN = r'^\d{2}-[A-Z-]+$'

def is_leaf_directory(path: Path) -> bool:
    """Check if directory is a leaf (contains .md files, not subdirectories)."""
    if not path.is_dir():
        return False
    
    # Check if it has any .md files
    has_md_files = any(f.suffix == '.md' for f in path.iterdir() if f.is_file())
    
    # Check if it has subdirectories (excluding .git)
    has_subdirs = any(d.is_dir() and not d.name.startswith('.') for d in path.iterdir())
    
    return has_md_files and not has_subdirs


def validate_leaf_directory(path: Path) -> list[str]:
    """Validate a leaf directory has correct structure."""
    errors = []
    
    # Get all .md files in directory
    md_files = {f.name for f in path.iterdir() if f.is_file() and f.suffix == '.md'}
    
    # Check for missing files
    missing = EXPECTED_FILES - md_files
    if missing:
        errors.append(f"Missing files in {path}: {', '.join(sorted(missing))}")
    
    # Check for unexpected files
    unexpected = md_files - EXPECTED_FILES
    if unexpected:
        errors.append(f"Unexpected files in {path}: {', '.join(sorted(unexpected))}")
    
    # Check for non-.md files (excluding hidden files)
    non_md = [f.name for f in path.iterdir() if f.is_file() and not f.name.startswith('.') and f.suffix != '.md']
    if non_md:
        errors.append(f"Non-markdown files in {path}: {', '.join(non_md)}")
    
    return errors


def find_leaf_directories(root: Path) -> list[Path]:
    """Find all leaf directories in domain folders."""
    leaf_dirs = []
    
    # Iterate through domain directories (01-XX)
    for domain_dir in sorted(root.iterdir()):
        if not domain_dir.is_dir():
            continue
        if not domain_dir.name[0].isdigit():
            continue
        
        # Walk through all subdirectories
        for dirpath, dirnames, filenames in os.walk(domain_dir):
            current_path = Path(dirpath)
            
            # Skip hidden directories
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            
            # Check if this is a leaf directory
            if is_leaf_directory(current_path):
                leaf_dirs.append(current_path)
    
    return leaf_dirs


def main():
    """Main validation function."""
    # Get repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    print("Validating repository structure...")
    print(f"Repository root: {repo_root}")
    print()
    
    # Find all leaf directories
    leaf_dirs = find_leaf_directories(repo_root)
    print(f"Found {len(leaf_dirs)} leaf directories")
    print()
    
    # Validate each leaf directory
    all_errors = []
    for leaf_dir in leaf_dirs:
        errors = validate_leaf_directory(leaf_dir)
        all_errors.extend(errors)
    
    # Report results
    if all_errors:
        print("❌ VALIDATION FAILED")
        print(f"\nFound {len(all_errors)} errors:\n")
        for error in all_errors:
            print(f"  • {error}")
        return 1
    else:
        print("✅ VALIDATION PASSED")
        print(f"All {len(leaf_dirs)} directories have correct structure")
        return 0


if __name__ == '__main__':
    sys.exit(main())
