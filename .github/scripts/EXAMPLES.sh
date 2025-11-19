#!/bin/bash
#
# Quick validation examples for common tasks
#

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  VALIDATION SCRIPTS - QUICK REFERENCE                         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo

# Example 1: Validate single file
echo -e "${BLUE}Example 1: Validate a single file${NC}"
echo "  python3 scripts/validate_formatting.py path/to/file.md"
echo "  python3 scripts/validate_content.py path/to/file.md"
echo

# Example 2: Validate all books
echo -e "${BLUE}Example 2: Validate all books.md files${NC}"
echo "  find [0-9]* -name 'books.md' | while read f; do"
echo "    python3 scripts/validate_formatting.py \"\$f\""
echo "  done"
echo

# Example 3: Check structure
echo -e "${BLUE}Example 3: Check repository structure${NC}"
echo "  python3 scripts/validate_structure.py"
echo

# Example 4: Find empty files
echo -e "${BLUE}Example 4: Find unfilled template files${NC}"
echo "  bash scripts/find_empty_files.sh"
echo

# Example 5: Check for duplicates
echo -e "${BLUE}Example 5: Check for duplicates in specific domain${NC}"
echo "  python3 scripts/check_duplicates.py 01-FUNDAMENTALS/"
echo

# Example 6: Generate statistics
echo -e "${BLUE}Example 6: Generate repository statistics${NC}"
echo "  python3 scripts/generate_statistics.py"
echo

# Example 7: Validate links (slow)
echo -e "${BLUE}Example 7: Validate links in a file${NC}"
echo "  python3 scripts/validate_links.py path/to/file.md"
echo "  python3 scripts/validate_links.py path/to/file.md --timeout 15 --parallel 10"
echo

# Example 8: Run all validations
echo -e "${BLUE}Example 8: Run all validation checks${NC}"
echo "  bash scripts/validate_all.sh"
echo

# Example 9: Validate PR changes
echo -e "${BLUE}Example 9: Validate changed files in git${NC}"
echo "  git diff --name-only main | grep '\\.md\$' | while read f; do"
echo "    [ -f \"\$f\" ] && python3 scripts/validate_formatting.py \"\$f\""
echo "  done"
echo

# Example 10: Count filled vs empty
echo -e "${BLUE}Example 10: Count filled vs empty files${NC}"
echo "  total=\$(find [0-9]* -name '*.md' | wc -l)"
echo "  empty=\$(grep -rl 'Add resources below' [0-9]* | wc -l)"
echo "  filled=\$((total - empty))"
echo "  echo \"Filled: \$filled / \$total\""
echo

echo -e "${GREEN}Run any of the above commands from the repository root.${NC}"
