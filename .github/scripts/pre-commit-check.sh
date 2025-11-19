#!/bin/bash
#
# Helper script for contributors to validate their changes before committing
# Usage: ./scripts/pre-commit-check.sh
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "🔍 Pre-commit validation check..."
echo

# Get list of staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$' || true)

if [ -z "$STAGED_FILES" ]; then
    echo "✅ No markdown files staged for commit"
    exit 0
fi

echo "Checking staged files:"
echo "$STAGED_FILES" | while read file; do echo "  • $file"; done
echo

FAILED=0

# Validate each staged file
for FILE in $STAGED_FILES; do
    # Skip files that don't exist (deleted files)
    if [ ! -f "$FILE" ]; then
        continue
    fi
    
    # Skip template and meta files
    if [[ "$FILE" == *"TEMPLATE"* ]] || [[ ! "$FILE" =~ ^[0-9] ]]; then
        continue
    fi
    
    echo "Validating: $FILE"
    
    # Format validation
    if ! python3 scripts/validate_formatting.py "$FILE" > /dev/null 2>&1; then
        echo "  ❌ Formatting issues detected"
        echo "     Run: python3 scripts/fix_formatting.py $FILE"
        FAILED=1
    else
        echo "  ✓ Formatting OK"
    fi
    
    # Content validation
    if ! python3 scripts/validate_content.py "$FILE" > /dev/null 2>&1; then
        echo "  ❌ Content issues detected"
        echo "     Run: python3 scripts/validate_content.py $FILE"
        FAILED=1
    else
        echo "  ✓ Content OK"
    fi
    
    echo
done

# Check for duplicates in changed domains
DOMAINS=$(echo "$STAGED_FILES" | cut -d'/' -f1 | sort -u)
for DOMAIN in $DOMAINS; do
    if [[ "$DOMAIN" =~ ^[0-9] ]]; then
        echo "Checking duplicates in $DOMAIN..."
        if ! python3 scripts/check_duplicates.py "$DOMAIN" > /dev/null 2>&1; then
            echo "  ⚠️  Duplicates detected (may be intentional)"
        else
            echo "  ✓ No duplicates"
        fi
    fi
done

echo
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $FAILED -eq 0 ]; then
    echo "✅ All checks passed! Ready to commit."
    exit 0
else
    echo "❌ Some checks failed. Please fix issues before committing."
    echo
    echo "Common fixes:"
    echo "  • Auto-fix formatting: python3 scripts/fix_formatting.py FILE"
    echo "  • View content errors: python3 scripts/validate_content.py FILE"
    echo "  • View format errors: python3 scripts/validate_formatting.py FILE"
    exit 1
fi
