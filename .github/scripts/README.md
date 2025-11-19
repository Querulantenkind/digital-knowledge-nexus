# Validation Scripts

This directory contains automated validation scripts for maintaining quality and consistency across the Digital Knowledge Nexus repository.

---

## Available Scripts

### validate_all.sh
**Purpose:** Runs all validation checks in sequence  
**Usage:** `./validate_all.sh`  
**Exit code:** 0 if all checks pass, 1 if any fail

### validate_structure.py
**Purpose:** Validates repository structure and file organization  
**Checks:**
- All category directories have exactly 8 format files
- File names match expected formats (books.md, papers.md, etc.)
- No unexpected files in category directories
- Directory structure matches FILETREE.md

**Usage:** `python3 validate_structure.py`

### validate_formatting.py
**Purpose:** Validates markdown formatting and style compliance  
**Checks:**
- Title capitalization (title case)
- URL format (includes https://)
- Required fields present
- Consistent spacing
- No trailing whitespace
- No emojis
- Proper difficulty section labels
- Field label capitalization

**Usage:** `python3 validate_formatting.py [file_path]`  
**Examples:**
```bash
# Validate single file
python3 validate_formatting.py 01-FUNDAMENTALS/computer-science/theory/computational-complexity/p-vs-np/books.md

# Validate all books.md files
find [0-9]* -name "books.md" -exec python3 validate_formatting.py {} \;
```

### validate_content.py
**Purpose:** Validates content quality and completeness  
**Checks:**
- URLs are accessible (not 404)
- ISBN format is valid
- DOI format is valid
- Years are reasonable (1950-2026)
- Descriptions are non-empty
- No duplicate entries in same file
- Template placeholders are replaced

**Usage:** `python3 validate_content.py [file_path]`

### validate_links.py
**Purpose:** Checks all URLs for accessibility  
**Checks:**
- HTTP status codes (warns on 404, 403, 500)
- HTTPS vs HTTP
- Redirect chains
- Slow response times

**Usage:** `python3 validate_links.py [file_path]`  
**Options:**
- `--timeout N` - Set timeout in seconds (default: 10)
- `--parallel N` - Number of parallel requests (default: 5)

### find_empty_files.sh
**Purpose:** Finds template files that haven't been filled with content  
**Usage:** `./find_empty_files.sh`  
**Output:** List of files containing template comment marker

### check_duplicates.py
**Purpose:** Finds duplicate entries across files  
**Checks:**
- Same title in multiple files
- Same URL in multiple entries
- Same ISBN/DOI in multiple entries

**Usage:** `python3 check_duplicates.py [directory]`

### generate_statistics.py
**Purpose:** Generates repository statistics  
**Output:**
- Total files and entries count
- Distribution by difficulty level
- Distribution by format type
- Distribution by year
- Coverage by domain

**Usage:** `python3 generate_statistics.py`

---

## GitHub Actions Integration

These scripts are integrated into GitHub Actions workflows:

### On Pull Request:
- `.github/workflows/validate-pr.yml`
- Runs structure, formatting, and content validation
- Blocks merge if validation fails

### Nightly:
- `.github/workflows/validate-links.yml`
- Checks all links for accessibility
- Creates issues for broken links

---

## Setup

### Requirements

**Python scripts require:**
```bash
pip install requests pyyaml markdown
```

**Bash scripts require:**
- grep
- find
- wc

### Installation

```bash
# Clone repository
git clone https://github.com/Querulantenkind/digital-knowledge-nexus.git
cd digital-knowledge-nexus

# Install Python dependencies
pip install -r scripts/requirements.txt

# Make scripts executable
chmod +x scripts/*.sh
```

---

## Contributing

When adding new validation checks:

1. Add script to this directory
2. Update this README
3. Add to `validate_all.sh` if appropriate
4. Consider GitHub Actions integration
5. Test on existing repository content

---

## Testing

Test validation scripts on known good and bad examples:

```bash
# Test on known good file
python3 validate_formatting.py 01-FUNDAMENTALS/computer-science/theory/computational-complexity/p-vs-np/books.md

# Test on template (should fail)
python3 validate_formatting.py TEMPLATES/template-book.md
```

---

Last Updated: 2025-11-19
