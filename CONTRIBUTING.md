# Contributing to Digital Knowledge Nexus

Thank you for contributing to this knowledge hub. This guide ensures all contributions maintain consistency and quality.

---

## Before You Start

1. Search existing content to avoid duplicates
2. Verify your resource is accessible (not broken link, not behind hard paywall)
3. Ensure resource is directly related to digital technology
4. Read the appropriate TEMPLATE file for your resource type

---

## Contribution Process

### Step 1: Find the Correct Location

Navigate the folder structure to find where your resource belongs:
```
Domain (01-12) → Category → Subcategory → Topic → Format File
```

**Example:** A book about Rust ownership system goes in:
```
02-SOFTWARE-ENGINEERING/programming-languages/systems-programming/rust/ownership-borrowing/books.md
```

**If you cannot find the right category:**
- Open an issue with "Category Request" template
- Do NOT create new folders without discussion
- Do NOT place resources in wrong categories "temporarily"

### Step 2: Choose the Correct Format File

Each topic has 8 format files:

- **books.md** - Published books, textbooks, technical guides
- **papers.md** - Academic papers, research papers, whitepapers, technical reports
- **courses.md** - Online courses, university curricula, structured tutorials
- **videos.md** - Conference talks, lectures, video series, screencasts
- **interactive.md** - Interactive tutorials, coding playgrounds, Jupyter notebooks, exercises
- **documentation.md** - Official documentation, API references, specifications, standards
- **tools.md** - Software, libraries, frameworks, command-line tools, applications
- **podcasts-blogs.md** - Podcasts, podcast episodes, blog series, newsletters

**One resource = One file.** If your resource fits multiple formats, choose the primary one.

### Step 3: Use the Correct Template

Open the TEMPLATES directory and copy the template for your format type:
```
TEMPLATES/
├── template-book.md
├── template-paper.md
├── template-course.md
├── template-video.md
├── template-interactive.md
├── template-documentation.md
├── template-tool.md
└── template-podcast-blog.md
```

### Step 4: Fill All Required Fields

Every field in the template is required. Incomplete entries will be rejected.

**Required for ALL formats:**
- Title (exact, official title)
- Author/Creator (full names)
- Year (publication or last update)
- Link (direct, working URL)
- Description (one-line summary)
- Why included (explicit justification)

**Additional fields vary by format** (see templates)

### Step 5: Choose the Correct Difficulty Section

Add your entry to ONE section:

**BEGINNER**
- Assumes minimal prior knowledge in this specific topic
- Introduces concepts with clear explanations
- Provides foundational understanding
- Examples: introductory textbooks, "getting started" guides

**INTERMEDIATE**
- Assumes solid foundation in the topic
- Covers practical applications and common patterns
- Goes beyond basics into real-world usage
- Examples: practical guides, implementation-focused resources

**ADVANCED**
- Assumes expert-level knowledge
- Covers edge cases, optimization, internals
- Research-level or production-scale content
- Examples: research papers, performance optimization guides

**CLASSIC**
- Foundational work that defined or shaped the field
- Widely cited or historically significant
- Still relevant despite age
- Examples: seminal papers, influential books

**RECENT (2023+)**
- Published or significantly updated since 2023
- Represents current state-of-the-art or best practices
- Must be substantive (not just blog posts announcing minor updates)

**If unsure between two sections, choose the lower difficulty level.**

### Step 6: Submit Pull Request

1. Fork the repository
2. Create a branch named: `add-[resource-type]-[topic]`
   - Example: `add-book-rust-ownership`
3. Make your changes
4. Commit with descriptive message: `Add [Title] to [Category/Topic/Format]`
5. Submit pull request using the template
6. Wait for review

---

## Contribution Rules

### ACCEPTED

- Resources directly about digital technology, computer science, hardware, software, AI
- Any publication date (if still relevant)
- Any language (description must be English)
- Free resources (preferred)
- Paid resources (if widely recognized as valuable)
- Resources requiring account/registration (if content is substantive)
- Multiple resources from same author (if each provides unique value)
- Translations of existing resources (if officially published)

### REJECTED

- Promotional content or marketing materials
- Resources primarily behind paywalls without free alternatives
- Duplicate entries (same content already listed)
- Off-topic content (business, self-help, non-technical)
- Incomplete entries (missing required fields)
- Wrong category placement
- Wrong format file
- Broken links (unless fixing with updated link)
- Personal blogs (unless established series with substantial content)
- Social media posts (unless archived substantial technical content)
- Resources requiring specific paid software to access content
- AI-generated content without expert review
- Tutorial mills or content farms
- Resources with malicious content

### EDGE CASES

**Q: Resource covers multiple topics. Where should it go?**
A: Choose the PRIMARY topic. Add a note in "Description" mentioning other topics covered.

**Q: Resource fits multiple formats (e.g., video course)?**
A: Choose the PRIMARY format. Video with structure → courses.md. Single talk → videos.md.

**Q: Resource is between two difficulty levels?**
A: Choose the LOWER level. Beginner/Intermediate → Beginner.

**Q: Classic resource was recently updated?**
A: If foundational nature unchanged → CLASSIC. If substantially modernized → RECENT.

**Q: Where do reference cards, cheat sheets go?**
A: documentation.md (if official) or interactive.md (if community-created)

**Q: Where do GitHub repositories go?**
A: tools.md (if it's a library/tool), interactive.md (if it's learning material)

---

## Formatting Standards

Follow the STYLE_GUIDE.md for:
- Title capitalization
- Name formatting
- Date formats
- Link formats
- Abbreviations

**Critical formatting rules:**

1. **Titles:** Use official title exactly as published
2. **Names:** Full names, no initials unless that's how they publish
3. **Years:** Four-digit year (2024, not '24 or 24)
4. **Links:** Full URL with protocol (https://example.com)
5. **Descriptions:** One sentence, no period at end
6. **Line breaks:** One blank line between entries
7. **No emojis** in entries
8. **No HTML** in markdown files
9. **Consistent field order** as shown in templates

---

## Quality Standards

### Good Entry Example
```markdown
### Programming Rust: Fast, Safe Systems Development
Author: Jim Blandy, Jason Orendorff, Leonora F. S. Tindall
Year: 2021
Publisher: O'Reilly Media
ISBN: 978-1492052593
Link: https://www.oreilly.com/library/view/programming-rust-2nd/9781492052586/
Description: Comprehensive guide to Rust programming with detailed coverage of ownership, concurrency, and systems programming concepts
Why included: Authoritative O'Reilly resource, thorough treatment of advanced topics, widely recommended by Rust community
```

### Bad Entry Example
```markdown
### Rust Book
Author: Steve
Year: 2023
Link: rust-lang.org/book
Description: Good book about Rust!!! 🦀
Why included: Everyone uses it
```

**Problems:**
- Incomplete title
- Incomplete author name
- Missing publisher/ISBN
- Incomplete URL (no protocol)
- Unprofessional description with emoji
- Vague justification

---

## Review Process

1. **Automated checks** verify formatting
2. **Community review** checks placement and quality
3. **Maintainer approval** required for merge

**Typical review time:** 2-7 days

**If your PR is rejected:**
- Read the rejection reason carefully
- Make requested changes
- Resubmit

**Do NOT:**
- Argue about category placement (structure is fixed)
- Submit same resource to multiple categories
- Bypass templates
- Create new categories without approval

---

## Special Cases

### Updating Existing Entries

**Fixing broken links:**
- Submit PR with updated link
- Note in commit message: "Fix broken link for [Title]"

**Updating outdated information:**
- Submit PR with corrections
- Note what changed in commit message

**DO NOT change structure or remove entries without discussion.**

### Dead Resources

If a resource is permanently unavailable:
- Open an issue (do not directly delete)
- Check Internet Archive / Wayback Machine for archive
- If archived version exists, update link
- If completely gone, maintainers will decide on removal

### Translations

Official translations can be added as separate entries:
```markdown
### [Original Title] (German Edition)
Author: Original Author (Translated by Translator Name)
...
```

---

## Questions?

- **Category placement:** Check INDEX.md or open Category Request issue
- **Format choice:** Check FAQ.md
- **Quality concerns:** Check QUALITY_CRITERIA.md
- **Citation format:** Check CITATION-GUIDE.md
- **Formatting:** Check STYLE_GUIDE.md

**Still stuck?** Open a "Question" issue.

---

## Code of Conduct

All contributors must follow CODE_OF_CONDUCT.md. Be professional, respectful, and collaborative.

---

Last Updated: 2025-11-19
