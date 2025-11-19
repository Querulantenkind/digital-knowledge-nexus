# Contributing Guide for AI Assistants

This guide helps AI assistants and automated tools contribute effectively to the Digital Knowledge Nexus.

---

## Quick Start for AI Assistants

### 1. Understanding the Structure

```
Repository Structure:
├── 01-FUNDAMENTALS/ (Computer Science, Math, etc.)
├── 02-SOFTWARE-ENGINEERING/ (Languages, Design, etc.)
├── 03-HARDWARE/ (Architecture, Embedded, etc.)
├── 04-ARTIFICIAL-INTELLIGENCE/ (ML, DL, NLP, etc.)
├── 05-SYSTEMS/ (OS, Networks, Distributed, etc.)
├── 06-SECURITY/ (Crypto, AppSec, etc.)
├── 07-DATA-SCIENCE/ (Analytics, Visualization, etc.)
├── 08-WEB-DEVELOPMENT/ (Frontend, Backend, etc.)
├── 09-MOBILE-DEVELOPMENT/ (iOS, Android, etc.)
├── 10-GAME-DEVELOPMENT/ (Engines, Graphics, etc.)
├── 11-SPECIALIZED-DOMAINS/ (Embedded, Quantum, etc.)
└── 12-META-SKILLS/ (Learning, Productivity, etc.)
```

Each leaf category has 8 format files:
- `books.md` - Published books, textbooks
- `papers.md` - Academic papers, research
- `courses.md` - Online courses, curricula
- `videos.md` - Talks, lectures, tutorials
- `interactive.md` - Coding playgrounds, exercises
- `documentation.md` - Official docs, specs
- `tools.md` - Software, libraries, frameworks
- `podcasts-blogs.md` - Podcasts, blog series

### 2. Before Adding Content

**Always run validation first:**
```bash
# Check file exists and structure
python3 scripts/validate_structure.py

# Validate existing content
python3 scripts/validate_content.py path/to/file.md
python3 scripts/validate_formatting.py path/to/file.md
```

### 3. Adding Resources

**Step-by-step workflow:**

1. **Read the template:**
   ```bash
   cat TEMPLATES/template-book.md  # or appropriate format
   ```

2. **Check existing content:**
   ```bash
   cat path/to/category/books.md
   ```

3. **Add your entry using exact template format:**
   - Use proper difficulty section (BEGINNER, INTERMEDIATE, ADVANCED, CLASSIC, RECENT)
   - Include ALL required fields
   - Follow STYLE-GUIDE.md for formatting

4. **Validate your changes:**
   ```bash
   python3 scripts/validate_formatting.py path/to/file.md
   python3 scripts/validate_content.py path/to/file.md
   ```

5. **Check for duplicates:**
   ```bash
   python3 scripts/check_duplicates.py path/to/domain/
   ```

### 4. Common Pitfalls for AI Assistants

❌ **DON'T:**
- Add multiple entries at once without validation
- Copy-paste similar entries without checking for duplicates
- Invent ISBNs, DOIs, or other identifiers
- Use placeholder text (YYYY, XXX, etc.)
- Add resources without verifying they exist
- Create new categories without approval
- Modify template structure

✅ **DO:**
- Validate after each addition
- Use real, verified URLs
- Check that resources are actually accessible
- Follow difficulty level guidelines strictly
- Maintain consistent formatting
- Use official resource titles exactly
- Include proper justification in "Why included"

### 5. Entry Quality Checklist

For each resource you add:

**Required:**
- [ ] Title is exact, official title
- [ ] Author/Creator is full name (not initials)
- [ ] Year is accurate (YYYY format)
- [ ] URL is direct link with https://
- [ ] Description is one clear sentence
- [ ] "Why included" explains value/uniqueness
- [ ] Placed in correct difficulty section
- [ ] All required fields for format type present

**Quality:**
- [ ] No trailing whitespace
- [ ] Title uses title case
- [ ] No emojis or decorative Unicode
- [ ] ISBN/DOI format is valid (if applicable)
- [ ] URL is accessible (not 404)
- [ ] Not a duplicate of existing entry
- [ ] Description is substantive (not generic)

### 6. Batch Operations

**When adding multiple resources:**

```python
# Pseudocode for AI assistants
for resource in resources_to_add:
    1. Verify resource exists and is accessible
    2. Check not already in repository
    3. Format according to template
    4. Add to appropriate section
    5. Validate entry
    6. If validation fails, fix and retry
    7. Only proceed to next if current validates

# After all additions
run("python3 scripts/check_duplicates.py .")
run("python3 scripts/validate_all.sh")
```

### 7. Automated Validation Hooks

**Before committing changes:**
```bash
# Fix common formatting issues automatically
python3 scripts/fix_formatting.py path/to/file.md

# Validate everything
bash scripts/validate_all.sh
```

### 8. Domain-Specific Notes

**01-FUNDAMENTALS:**
- Focus on timeless, foundational concepts
- Prefer classic textbooks and papers
- Include historical context

**04-ARTIFICIAL-INTELLIGENCE:**
- Rapidly evolving - balance classic vs recent
- Include both theory and implementation
- Note framework/library versions when relevant

**12-META-SKILLS:**
- Focus on learning techniques, not content
- Include cognitive science backing
- Emphasize evidence-based methods

### 9. Difficulty Level Guidelines for AI

**BEGINNER:**
```python
if (assumes_no_prior_knowledge and 
    explains_basics_clearly and 
    uses_simple_examples):
    section = "BEGINNER"
```

**INTERMEDIATE:**
```python
if (assumes_foundation and 
    covers_practical_applications and 
    requires_some_experience):
    section = "INTERMEDIATE"
```

**ADVANCED:**
```python
if (assumes_expertise and 
    covers_edge_cases_or_research and 
    requires_strong_background):
    section = "ADVANCED"
```

**CLASSIC:**
```python
if (published_5plus_years_ago and 
    foundational_importance and 
    still_widely_referenced):
    section = "CLASSIC"
```

**RECENT (2023+):**
```python
if (published_2023_or_later and 
    substantive_content and 
    represents_current_state):
    section = "RECENT (2023+)"
```

### 10. Error Recovery

**If validation fails:**

1. **Read the error message carefully**
2. **Common fixes:**
   - Trailing whitespace: Run `fix_formatting.py`
   - Missing field: Add from template
   - Invalid URL: Verify and correct
   - Duplicate: Check if intentional cross-reference
3. **Re-validate after each fix**
4. **Don't proceed until validation passes**

### 11. Progress Tracking

**Check repository status:**
```bash
# Overall statistics
python3 scripts/generate_statistics.py

# Detailed progress report
python3 scripts/progress_report.py

# Find empty files
bash scripts/find_empty_files.sh
```

### 12. Best Practices for Content Generation

**Research Quality:**
- Verify resources exist before adding
- Check publication dates are accurate
- Confirm URLs are accessible
- Validate ISBNs/DOIs if provided

**Content Organization:**
- One resource = one entry = one file
- Place in most specific category
- Use primary format if resource fits multiple

**Consistency:**
- Follow existing entries as examples
- Maintain same structure across files
- Use consistent terminology

### 13. Testing Your Changes

**Minimal test before submitting:**
```bash
# Structure check
python3 scripts/validate_structure.py

# Format check on changed file
python3 scripts/validate_formatting.py YOUR_FILE.md

# Content check on changed file
python3 scripts/validate_content.py YOUR_FILE.md

# Duplicate check in domain
python3 scripts/check_duplicates.py YOUR_DOMAIN/
```

### 14. Workflow Summary

```
1. Identify category and format
2. Read template for format type
3. Check existing entries in file
4. Research and verify resource
5. Format entry according to template
6. Add to appropriate difficulty section
7. Run validation scripts
8. Fix any errors
9. Re-validate
10. Proceed to next resource
```

---

## Quick Reference Commands

```bash
# Validation
python3 scripts/validate_all.sh                    # All checks
python3 scripts/validate_structure.py              # Structure only
python3 scripts/validate_formatting.py FILE        # Format check
python3 scripts/validate_content.py FILE           # Content check
python3 scripts/check_duplicates.py DIR            # Duplicates

# Statistics
python3 scripts/generate_statistics.py             # Overall stats
python3 scripts/progress_report.py                 # Progress report
bash scripts/find_empty_files.sh                   # Empty templates

# Utilities
python3 scripts/fix_formatting.py FILE             # Auto-fix format
bash scripts/EXAMPLES.sh                           # Show examples
```

---

Last Updated: 2025-11-19
