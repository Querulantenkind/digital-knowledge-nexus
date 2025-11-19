#!/bin/bash
#
# Find empty template files that haven't been filled with content.
# Usage: ./find_empty_files.sh
#

echo "Finding empty template files..."
echo

# Count total format files
total=$(find [0-9]* -name "*.md" -type f 2>/dev/null | wc -l)
echo "Total files: $total"

# Find files with template comment marker
echo "Searching for unfilled templates..."
empty=$(grep -r "Add resources below" [0-9]* 2>/dev/null | cut -d: -f1 | sort | uniq)

# Count empty files
empty_count=$(echo "$empty" | grep -c "^")

if [ $empty_count -eq 0 ]; then
    echo "✅ No empty template files found"
    exit 0
fi

echo "❌ Found $empty_count empty template files:"
echo
echo "$empty"

# Calculate percentage
filled=$((total - empty_count))
percentage=$((filled * 100 / total))

echo
echo "Progress: $filled/$total files filled ($percentage%)"

exit 0
