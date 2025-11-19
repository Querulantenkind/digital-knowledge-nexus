# Style Guide

Consistent formatting ensures readability and professionalism. All contributions must follow these style rules.

---

## General Formatting

### Line Length
- No hard line length limit
- Break for readability at natural points
- Keep descriptions to one line when possible

### Spacing
- One blank line between entries
- Two blank lines between sections
- No trailing whitespace
- File ends with single newline

### Character Encoding
- UTF-8 encoding for all files
- Use Unicode characters where appropriate (é, ñ, etc.)
- No smart quotes or em dashes (use straight quotes and hyphens)

---

## Titles

### Capitalization
Use **title case** for all titles (books, papers, courses, etc.):
- Capitalize first and last words
- Capitalize all major words (nouns, verbs, adjectives, adverbs)
- Lowercase articles (a, an, the)
- Lowercase coordinating conjunctions (and, but, or, nor, for, so, yet)
- Lowercase prepositions (in, on, at, to, for, with, from, of) UNLESS 4+ letters

**Examples:**
```
Correct: The Art of Computer Programming
Correct: Introduction to Algorithms
Correct: Compilers: Principles, Techniques, and Tools
Correct: Design Patterns: Elements of Reusable Object-Oriented Software
Correct: Operating Systems: Three Easy Pieces

Incorrect: The art of computer programming
Incorrect: Introduction To Algorithms
Incorrect: Design patterns: elements of reusable object-oriented software
```

### Subtitles
- Include subtitle after colon
- Maintain title case for subtitle
- Space before and after colon

**Example:**
```
### Computer Architecture: A Quantitative Approach
```

### Acronyms in Titles
- Preserve official capitalization
- Common: API, CPU, GPU, SQL, HTML, CSS, HTTP, TCP/IP

**Examples:**
```
### Understanding the Linux Kernel
### TCP/IP Illustrated
### SQL Performance Explained
```

---

## Names

### Author Names
- **Full names**: First Middle Last
- Multiple authors: comma-separated
- Maintain original name order
- Include suffix if used professionally (Jr., Sr., III)

**Format:**
```
Author: Brian W. Kernighan, Dennis M. Ritchie
Author: Andrew S. Tanenbaum
Author: Martin Fowler, Kent Beck, John Brant, William Opdyke, Don Roberts
```

### Single Name (No Exceptions)
```
Author: Euclid
Author: Plato
```

### Institutional Authors
```
Author: IEEE Computer Society
Author: W3C Working Group
Creator: Rust Project Team
```

### Handling Uncertainty
- If full name unknown, use what's available
- If only username/handle known: use that consistently
- Note: "Known by handle only" if needed

---

## Dates and Years

### Format
- **Year only** for most entries: 2024
- **Full date** for blog posts/podcasts: 2024-11-19 (ISO 8601)
- **Date ranges** for ongoing: 2020-Present

### Special Cases
```
Year: 2023 (Original: 1968)  # For updated classics
Year: Living Document         # For continuously updated
Year: 2024-Present           # For active projects
```

---

## Links

### URL Format
- **Always include protocol**: https://example.com
- **Never** use: example.com or www.example.com (without protocol)
- Use direct links (not redirects or shorteners)
- Prefer HTTPS over HTTP
- Remove tracking parameters when possible

**Examples:**
```
Correct: https://github.com/rust-lang/rust
Correct: https://arxiv.org/abs/1706.03762
Correct: https://www.youtube.com/watch?v=8pTEmbeENF4

Incorrect: github.com/rust-lang/rust
Incorrect: www.arxiv.org/abs/1706.03762
Incorrect: bit.ly/abc123
Incorrect: https://example.com?utm_source=...
```

### Special Link Cases

**DOI Links:**
```
DOI: 10.1145/1327452.1327492
Link: https://doi.org/10.1145/1327452.1327492
```

**arXiv:**
```
arXiv: 1706.03762
Link: https://arxiv.org/abs/1706.03762
(Prefer abs link over PDF link)
```

**GitHub:**
```
Link: https://github.com/user/repo
(Not: https://github.com/user/repo.git)
```

---

## Identifiers

### ISBN
- **Prefer ISBN-13**: 978-XXXXXXXXXX
- Include hyphens for readability
- Format: 978-X-XXX-XXXXX-X

**Examples:**
```
ISBN: 978-0-201-63361-0
ISBN: 978-1-4920-5259-3
```

### DOI
- Format: 10.XXXX/...
- No "doi:" prefix in field
- Include actual link separately
```
DOI: 10.1145/1327452.1327492
```

### arXiv ID
- New format (2007+): YYMM.NNNNN
- Old format: subject-class/YYMMNNN
```
arXiv: 1706.03762
arXiv: cs.LG/0001001  # Old format
```

---

## Descriptions

### Structure
- **One sentence** when possible
- No period at end (unless multiple sentences)
- Present tense
- Focus on content/scope, not opinion

**Good:**
```
Description: Comprehensive guide to Rust covering ownership, lifetimes, and concurrency with practical examples
Description: Introduces transformer architecture using self-attention mechanism without recurrence
Description: Interactive tutorial covering dynamic programming through visualization and practice problems
```

**Bad:**
```
Description: Amazing book!
Description: This is the best resource ever.
Description: Everyone should read this.
Description: The author explains things really well...
```

### Key Elements to Include
- Primary topic/scope
- Approach or methodology
- Key concepts covered
- Target audience (if notably specific)

---

## Field Labels

### Capitalization
- Use exact field names from templates
- Capitalize first word only

**Correct Format:**
```
Author: Name
Year: 2024
Publisher: Company
Link: https://...
Description: Text
Why included: Text
```

### Required vs Optional
- Templates show required fields
- Optional fields can be omitted
- Don't add custom fields

---

## Abbreviations

### When to Abbreviate
- Common technical terms: OK to abbreviate
- First use: spell out with abbreviation in parentheses
- Subsequent uses: abbreviation OK

**Standard Abbreviations:**
```
API - Application Programming Interface
CPU - Central Processing Unit
GPU - Graphics Processing Unit
RAM - Random Access Memory
OS - Operating System
ML - Machine Learning
DL - Deep Learning
NLP - Natural Language Processing
SQL - Structured Query Language
HTTP - Hypertext Transfer Protocol
TCP - Transmission Control Protocol
IP - Internet Protocol
```

### Conference/Journal Names
- Spell out full name first
- Include abbreviation in parentheses
- Use abbreviation in subsequent references
```
Venue: Conference on Neural Information Processing Systems (NeurIPS)
Venue: International Conference on Software Engineering (ICSE)
Venue: Association for Computing Machinery (ACM)
```

---

## Numbers

### General Rules
- Spell out one through nine
- Use numerals for 10+
- Use numerals for technical values

**Examples:**
```
Description: Covers five major design patterns
Description: Contains 20 chapters covering algorithms
Duration: 45 minutes
Prerequisites: Three years of programming experience
Version: 3.11
```

### Technical Numbers
```
Version: 1.0.0
Duration: 2 hours 30 minutes
Pages: 1,200
Year: 2024
```

---

## Punctuation

### Commas
- Oxford comma for lists of three or more
- After introductory phrases

**Examples:**
```
Author: John Smith, Jane Doe, and Bob Johnson
Description: Covers algorithms, data structures, and complexity theory
```

### Colons
- Space before and after in titles
- No space in time notation
```
### Title: Subtitle
Duration: 1:30:45
```

### Hyphens and Dashes
- Hyphen (-) for compound words
- En dash (–) for ranges (or use hyphen in plain text)
- No em dashes
```
Description: State-of-the-art methods
Year: 2020-2024
Duration: 45-60 minutes
```

---

## Markdown Formatting

### Headers
- Use ### for entry titles
- Use ## for section headers
- Use # only for file title

### Bold and Italics
- **Bold** for field labels
- *Italics* for emphasis (use sparingly)
- No bold or italics in entry titles

### Links
- Use full URLs, not relative paths
- Format: `[Text](URL)` only when needed for readability
- In structured entries, raw URLs are fine

### Lists
- Dash (-) for unordered lists
- Numbers for ordered lists
- Consistent indentation (2 spaces)

---

## Special Characters

### Allowed
- Standard Unicode letters (é, ñ, ü, etc.)
- Mathematical symbols (∀, ∃, ∈, etc.) when necessary
- Currency symbols ($, €, £)

### Not Allowed
- Emojis (🚀, 💻, etc.)
- Smart quotes (" " ' ')
- Em dashes (—)
- Decorative Unicode

**Replace:**
```
Bad: "Smart quotes"
Good: "Straight quotes"

Bad: Em-dash—like this
Good: Hyphen - like this

Bad: 🚀 Amazing resource!
Good: Comprehensive resource
```

---

## File Names

### Category Folders
- lowercase-with-hyphens
- No spaces, underscores, or camelCase
- Descriptive and concise

**Examples:**
```
machine-learning/
computer-architecture/
functional-programming/
```

### Format Files
- lowercase
- .md extension
- Match exactly:
```
books.md
papers.md
courses.md
videos.md
interactive.md
documentation.md
tools.md
podcasts-blogs.md
```

---

## Consistency Checklist

Before submitting, verify:

- [ ] Title case for all titles
- [ ] Full author names
- [ ] Four-digit years
- [ ] URLs include https://
- [ ] No emojis anywhere
- [ ] One-sentence descriptions
- [ ] Field labels match template
- [ ] Consistent spacing
- [ ] No trailing whitespace
- [ ] File ends with newline

---

Last Updated: 2025-11-19
