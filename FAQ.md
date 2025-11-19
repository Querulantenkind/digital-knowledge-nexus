# Frequently Asked Questions

Common questions about contributing to and using Digital Knowledge Nexus.

---

## General Questions

### What is Digital Knowledge Nexus?

A community-curated bibliography of technical resources for computer science, software engineering, hardware, AI, and related fields. It's organized by topic and format to help learners and professionals find high-quality resources.

### Who is this for?

Everyone involved in technology: students, professionals, researchers, educators, and self-learners. Resources range from beginner to advanced levels.

### Is this like Awesome Lists?

Similar concept, but with much deeper categorization (1,600+ categories vs. typically 10-50) and stricter formatting through templates. The goal is comprehensive coverage with precise placement.

### How is this different from other resource collections?

**Unique features:**
- 3-5 level deep categorization
- Separate files for each format type (books vs papers vs courses)
- Strict templates for consistency
- No quality gatekeeping - clear rules instead
- Massive scale by design (40,000+ resource capacity)

---

## Using the Repository

### How do I find resources on a specific topic?

**Method 1: Browse**
1. Navigate through folders starting from numbered domains (01-12)
2. Drill down to your specific topic
3. Choose format file (books.md, papers.md, etc.)

**Method 2: Search**
1. Press `/` on GitHub
2. Type topic keywords
3. Look for .md files in relevant paths

**Method 3: Index**
1. Check INDEX.md for complete category tree
2. Click links to navigate directly

### What if I can't find my topic?

1. Check INDEX.md - it might be named differently
2. Search for related keywords
3. If truly missing, open a Category Request issue

### Which format file should I look at?

**Choose based on your learning style:**
- books.md → Comprehensive, structured learning
- papers.md → Research-level depth, original findings
- courses.md → Structured learning with exercises
- videos.md → Visual/auditory learning, talks
- interactive.md → Hands-on practice, experimentation
- documentation.md → Reference, specifications
- tools.md → Practical implementation, software
- podcasts-blogs.md → Casual learning, ongoing topics

### What do the difficulty levels mean?

- **BEGINNER** - Introductory, minimal prerequisites
- **INTERMEDIATE** - Solid foundation required, practical focus
- **ADVANCED** - Expert level, cutting-edge or highly technical
- **CLASSIC** - Foundational work, historical significance
- **RECENT (2023+)** - Latest developments and techniques

### Can I suggest a resource without making a pull request?

Yes! Open a Resource Submission issue with the resource details. Someone else may create the pull request, or we can guide you through the process.

---

## Contributing

### I'm new to GitHub. How do I contribute?

**Simple approach:**
1. Open a Resource Submission issue
2. Fill in the template
3. Community or maintainers will handle the pull request

**Learn GitHub approach:**
1. Read GitHub's "Hello World" guide
2. Fork this repository
3. Follow CONTRIBUTING.md
4. Submit your first pull request

We're happy to help newcomers!

### Do I need permission to contribute?

No! This is an open project. Just follow the guidelines in CONTRIBUTING.md and submit a pull request.

### How long does it take for contributions to be reviewed?

Typically 2-7 days. Complex cases or structural changes may take longer.

### My pull request was rejected. What now?

Read the rejection reason carefully. Common issues:
- Wrong category placement
- Missing required fields
- Duplicate resource
- Quality concerns

Fix the issues and resubmit.

### Can I contribute resources in languages other than English?

Yes! Resources can be in any language, but:
- Description must be in English
- All metadata must be in English
- Note the language in the description

---

## Category Placement

### My resource covers multiple topics. Where should it go?

Choose the PRIMARY topic. Mention other topics in the description.

**Example:**
A book on "Deep Learning for Computer Vision" goes in:
- Primary: 04-ARTIFICIAL-INTELLIGENCE/computer-vision/
- Note in description: "Covers deep learning techniques"

### What if a resource fits multiple categories equally?

1. Check if one category is more specific (choose more specific)
2. Check which category has fewer resources (choose less populated)
3. If still unclear, open an issue to discuss

**Don't add to multiple categories** - causes maintenance issues.

### The perfect category doesn't exist. What do I do?

**Option 1:** Place in closest existing category
**Option 2:** Open a Category Request issue

**Don't create new folders without approval.**

### How deep should categories go?

Current structure goes 3-5 levels deep. We aim for:
- Enough specificity to be useful
- Not so specific that categories have 1-2 resources

**Examples:**
```
Too shallow: SOFTWARE-ENGINEERING/programming/
Just right: SOFTWARE-ENGINEERING/programming-languages/systems-programming/rust/
Too deep: SOFTWARE-ENGINEERING/programming-languages/systems-programming/rust/ownership/lifetimes/elision/
```

---

## Format Questions

### Is this a book or a course?

**Books:**
- Published as a book (physical or electronic)
- Read sequentially
- No exercises beyond book content

**Courses:**
- Structured curriculum
- Lectures + exercises + assignments
- Typically time-bound or self-paced

**Borderline cases:**
- O'Reilly "book" with video content → books.md (if primarily text)
- Course based on a book → courses.md (if has separate exercises)

### Where do conference talks go?

videos.md - Conference talks are presentations, not courses.

### Where do GitHub repositories go?

**Depends on content:**
- Library/Framework → tools.md
- Tutorial/Learning resource → interactive.md
- Documentation → documentation.md
- Research code → papers.md (link to paper, mention code in description)

### Where do Jupyter notebooks go?

interactive.md - They're hands-on learning resources.

### Where do blog posts go?

**Single post:** Generally don't include unless exceptionally influential
**Blog series:** podcasts-blogs.md
**Technical blog (ongoing):** podcasts-blogs.md

### What about podcasts?

**Full podcast series:** podcasts-blogs.md
**Single exceptional episode:** podcasts-blogs.md with episode noted

### Where do technical specifications go?

documentation.md - Specifications are reference documentation.

---

## Quality Questions

### What if a resource is outdated?

**Classic resources:** Include anyway, note "historical significance"
**Recent resources:** Consider if:
- Principles still apply?
- Better alternatives exist?
- Worth reading for perspective?

### Can I add my own work?

Yes, if it meets quality criteria. Be honest about:
- Why it's valuable
- How it compares to alternatives
- Your relationship to the work

Self-promotion for its own sake will be rejected.

### What about resources behind paywalls?

**Acceptable if:**
- Widely recognized as valuable
- Free preview available
- No free alternative of equal quality

**Note paywall in description** if not obvious.

### How many resources should be in each category?

**No hard limits**, but:
- 5-10 resources → well-curated
- 10-25 resources → comprehensive
- 25+ resources → may need subcategories

Quality over quantity always.

### Can I add multiple resources from the same author?

Yes, if each provides unique value. Don't add:
- Multiple editions (choose one)
- Overlapping content
- Redundant resources

---

## Technical Questions

### Why markdown instead of a database?

**Benefits:**
- Simple: anyone can edit text files
- Version controlled: full history in Git
- No build step: works without tools
- Searchable: GitHub's built-in search
- Forkable: easy to customize

### Why no search function?

- Keeps it simple (no build tools, no server)
- GitHub search works well
- Can be added later without changing structure
- Structure itself aids navigation

### Why 8 specific format files?

These cover ~95% of technical resources while remaining manageable:
- Books: written comprehensive guides
- Papers: research and technical reports
- Courses: structured learning
- Videos: presentations and talks
- Interactive: hands-on learning
- Documentation: specifications and references
- Tools: software and utilities
- Podcasts-Blogs: ongoing content

### Can the structure change?

**Minor changes:** Yes (clarifications, new subcategories)
**Major changes:** Rarely (requires strong justification)

Structure stability is important for usability.

---

## Collaboration

### How can I help beyond adding resources?

- Review pull requests
- Fix broken links
- Update outdated information
- Improve documentation
- Answer questions in issues
- Help newcomers

### Who maintains this?

Community-driven with minimal central maintenance. No gatekeepers, just clear rules.

### What if I disagree with a decision?

1. Open an issue to discuss
2. Provide clear reasoning
3. Be respectful
4. Accept that not all opinions will prevail

Focus on what's best for users of the repository.

### Can I fork and customize this?

**Absolutely!** That's the point of open source. You can:
- Fork and modify structure
- Add your own categories
- Use different quality criteria
- Build search tools on top

Just respect the license (CC0 for structure).

---

## Common Mistakes

### Don't:
1. Create new folders without approval
2. Add same resource to multiple categories
3. Skip required fields
4. Use marketing language in descriptions
5. Add resources you haven't verified
6. Ignore the templates
7. Assume category placement without checking
8. Get discouraged by rejection

### Do:
1. Read CONTRIBUTING.md first
2. Check for duplicates
3. Follow templates exactly
4. Provide clear justifications
5. Ask questions when unsure
6. Be patient with review process
7. Learn from feedback
8. Help others once you understand

---

## Getting Help

### Where do I ask questions?

1. Check this FAQ
2. Check CONTRIBUTING.md
3. Check INDEX.md for category questions
4. Open a Question issue
5. Check existing issues

### Who do I contact for urgent issues?

Open an issue with appropriate label:
- Broken link → Error Report
- Misplaced content → Error Report
- Malicious content → Security
- Harassment → Code of Conduct violation

### I found a security issue. What do I do?

See SECURITY.md for reporting procedures. Don't open public issues for security concerns.

---

## Philosophy

### Why is the structure so rigid?

Rigid structure enables:
- Consistent user experience
- Easy contribution (no ambiguity)
- Massive scale without chaos
- No gatekeeping needed
- Long-term maintainability

### Why no subjective quality control?

**Instead of subjective judgment:**
- Clear, objective criteria
- Templates enforce quality
- Community reviews
- Users judge for themselves

This scales better and avoids gatekeeping.

### What's the long-term vision?

A comprehensive, community-maintained knowledge graph of technical resources that:
- Helps learners find their path
- Gives professionals quick reference
- Preserves historical knowledge
- Adapts to new developments
- Requires minimal maintenance

---

## Still Have Questions?

Open a Question issue with:
- What you've already tried
- Specific details of your question
- Relevant context

We're here to help!

---

Last Updated: 2025-11-19
```

---

## 12. .gitignore
```
# Operating System Files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
Desktop.ini

# Editor Files
.vscode/
.idea/
*.swp
*.swo
*~
.vim/
*.sublime-project
*.sublime-workspace
.project
.settings/
.classpath

# Temporary Files
*.tmp
*.temp
*.log
*.bak
*.backup

# Node modules (if build tools added later)
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Python (if automation scripts added)
__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/
ENV/

# Build outputs (if website added later)
dist/
build/
*.egg-info/
.cache/

# Lock files (optional, depends on policy)
# package-lock.json
# yarn.lock

# Local configuration
.env
.env.local
config.local.*

# Testing
coverage/
.nyc_output/

# Documentation builds
docs/_build/
site/

# Archives
*.zip
*.tar.gz
*.rar

# Backups
*.orig