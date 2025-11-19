#!/bin/bash
#
# Run all validation checks in sequence.
# Usage: ./validate_all.sh
#

set -e  # Exit on first error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  DIGITAL KNOWLEDGE NEXUS - VALIDATION SUITE                   ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track results
PASSED=0
FAILED=0
WARNINGS=0

# Function to run a check
run_check() {
    local name=$1
    local command=$2
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Running: $name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    if eval "$command"; then
        echo -e "${GREEN}✅ PASSED${NC}: $name"
        ((PASSED++))
    else
        echo -e "${RED}❌ FAILED${NC}: $name"
        ((FAILED++))
    fi
    echo
}

# Check Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is required but not installed${NC}"
    exit 1
fi

# Check Python dependencies
echo "Checking dependencies..."
if ! python3 -c "import requests" 2>/dev/null; then
    echo -e "${YELLOW}⚠ Warning: 'requests' library not installed. Link validation will be skipped.${NC}"
    echo "Install with: pip install -r scripts/requirements.txt"
    ((WARNINGS++))
fi
echo

# Run structure validation
run_check "Structure Validation" "python3 scripts/validate_structure.py"

# Run formatting validation on sample files
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Running: Format Validation (sample files)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

FORMAT_FAILED=0
FORMAT_CHECKED=0

# Find filled files (non-template files)
for file in $(find [0-9]* -name "*.md" -type f | head -20); do
    # Skip empty template files
    if grep -q "Add resources below" "$file" 2>/dev/null; then
        continue
    fi
    
    ((FORMAT_CHECKED++))
    
    if ! python3 scripts/validate_formatting.py "$file" > /dev/null 2>&1; then
        echo -e "${RED}  ❌ $file${NC}"
        ((FORMAT_FAILED++))
    else
        echo -e "${GREEN}  ✓${NC} $file"
    fi
done

if [ $FORMAT_FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ PASSED${NC}: Format Validation ($FORMAT_CHECKED files checked)"
    ((PASSED++))
else
    echo -e "${RED}❌ FAILED${NC}: Format Validation ($FORMAT_FAILED/$FORMAT_CHECKED files failed)"
    ((FAILED++))
fi
echo

# Run content validation on sample files
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Running: Content Validation (sample files)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

CONTENT_FAILED=0
CONTENT_CHECKED=0

# Check same sample files
for file in $(find [0-9]* -name "*.md" -type f | head -20); do
    # Skip empty template files
    if grep -q "Add resources below" "$file" 2>/dev/null; then
        continue
    fi
    
    ((CONTENT_CHECKED++))
    
    if ! python3 scripts/validate_content.py "$file" > /dev/null 2>&1; then
        echo -e "${RED}  ❌ $file${NC}"
        ((CONTENT_FAILED++))
    else
        echo -e "${GREEN}  ✓${NC} $file"
    fi
done

if [ $CONTENT_FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ PASSED${NC}: Content Validation ($CONTENT_CHECKED files checked)"
    ((PASSED++))
else
    echo -e "${RED}❌ FAILED${NC}: Content Validation ($CONTENT_FAILED/$CONTENT_CHECKED files failed)"
    ((FAILED++))
fi
echo

# Check for duplicates
run_check "Duplicate Check" "python3 scripts/check_duplicates.py ."

# Find empty files
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Running: Empty Template Check"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

bash scripts/find_empty_files.sh
echo

# Print final summary
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  VALIDATION SUMMARY                                            ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo
echo -e "  ${GREEN}Passed${NC}: $PASSED"
echo -e "  ${RED}Failed${NC}: $FAILED"
echo -e "  ${YELLOW}Warnings${NC}: $WARNINGS"
echo

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ ALL VALIDATIONS PASSED${NC}"
    exit 0
else
    echo -e "${RED}❌ SOME VALIDATIONS FAILED${NC}"
    exit 1
fi
