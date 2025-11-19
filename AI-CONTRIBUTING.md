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

**Manual validation steps:**

1. Check the template in `/TEMPLATES/` for the correct format type
2. Review existing entries in the target file for formatting patterns
3. Verify all required fields are present
4. Ensure proper difficulty level placement
5. Check for duplicate entries manually

**Note:** Automated validation scripts are in development. For now, follow the templates strictly and review existing files for consistency.

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

4. **Validate your changes manually:**
   - Check all required fields are present
   - Verify formatting matches template
   - Ensure no trailing whitespace
   - Confirm proper title case
   - Validate URLs are accessible

5. **Check for duplicates:**
   - Search existing file for similar titles
   - Check ISBNs/DOIs aren't already present
   - Review related categories for cross-references

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
    2. Check not already in repository (manual search)
    3. Format according to template
    4. Add to appropriate section
    5. Review entry against quality checklist
    6. If issues found, fix and retry
    7. Only proceed to next if current passes review
```

### 7. Manual Quality Checks

**Before committing changes:**
- Review all entries against template format
- Check for trailing whitespace: `sed -i 's/[[:space:]]*$//' file.md`
- Verify all URLs are accessible
- Ensure consistent formatting across entries
- Confirm proper difficulty level placement

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

**Check repository status manually:**
```bash
# Count filled files (non-template entries)
find 01-FUNDAMENTALS -name "*.md" -type f ! -exec grep -q "Add resources below" {} \; -print | wc -l

# Find empty template files
find 01-FUNDAMENTALS -name "*.md" -type f -exec grep -q "Add resources below" {} \; -print

# Count total categories
find 01-FUNDAMENTALS -type d -mindepth 3 | wc -l
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

**Manual checks before submitting:**

1. **Structure check:** Verify file is in correct category path
2. **Format check:** Compare against template in `/TEMPLATES/`
3. **Content check:** Ensure all required fields present
4. **Duplicate check:** Search file for similar entries
5. **Link check:** Click URLs to verify accessibility
6. **Whitespace check:** `grep -n "[[:space:]]$" YOUR_FILE.md` (should return nothing)

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
# Manual validation helpers
grep -n "[[:space:]]$" FILE.md                    # Find trailing whitespace
sed -i 's/[[:space:]]*$//' FILE.md                # Remove trailing whitespace
grep -q "Add resources below" FILE.md && echo "Empty template"  # Check if filled

# Statistics
find 01-FUNDAMENTALS -name "*.md" -type f ! -exec grep -q "Add resources below" {} \; -print | wc -l  # Filled files
find 01-FUNDAMENTALS -type d -mindepth 3 | wc -l  # Total categories

# Search utilities
grep -r "SEARCH_TERM" 01-FUNDAMENTALS/            # Find existing entries
find . -name "*.md" -exec grep -l "ISBN" {} \;    # Find by ISBN
```

---

## Future Enhancements

Automated validation scripts are planned to be added in a `/scripts` directory:
- Structure validation
- Format validation
- Content validation  
- Duplicate detection
- Link checking
- Statistics generation

GitHub Actions workflows are configured to use these scripts when available.

---

Last Updated: 2025-11-19
