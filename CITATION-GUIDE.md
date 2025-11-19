# Citation Guide

Proper citation ensures credibility and helps others find resources. This guide covers how to cite different resource types in Digital Knowledge Nexus.

---

## General Principles

1. **Use official titles** - Exact as published, including capitalization
2. **Full names** - Complete author/creator names, no initials unless that's how they publish
3. **Direct links** - URL to the actual resource, not intermediaries
4. **Verifiable information** - All fields must be checkable
5. **Consistent format** - Follow templates exactly

---

## Books

### Required Fields
```markdown
### Title: Subtitle if Present
Author: First Last, First Last (multiple authors separated by commas)
Year: YYYY (publication year of edition you're citing)
Publisher: Publisher Name
ISBN: 978-XXXXXXXXXX (13-digit preferred, 10-digit acceptable)
Link: https://direct-link-to-book.com
Description: One-sentence summary of scope and content
Why included: What makes this resource valuable or unique
```

### Examples

**Single Author:**
```markdown
### Computer Systems: A Programmer's Perspective
Author: Randal E. Bryant, David R. O'Hallaron
Year: 2015
Publisher: Pearson
ISBN: 978-0134092669
Link: https://csapp.cs.cmu.edu/
Description: Comprehensive systems programming text covering computer architecture, operating systems, and networking from programmer's perspective
Why included: Standard university textbook, balances theory and practice, includes hands-on labs
```

**Multiple Editions:**
```markdown
### The C Programming Language
Author: Brian W. Kernighan, Dennis M. Ritchie
Year: 1988
Publisher: Prentice Hall
Edition: 2nd Edition
ISBN: 978-0131103627
Link: https://www.pearson.com/...
Description: Definitive C language reference by language creators
Why included: Canonical C resource, written by language designers, establishes C idioms
```

**Online Book:**
```markdown
### The Rust Programming Language
Author: Steve Klabnik, Carol Nichols
Year: 2023
Publisher: No Starch Press
ISBN: 978-1718503105
Link: https://doc.rust-lang.org/book/
Description: Official Rust book covering ownership, lifetimes, and systems programming concepts
Why included: Official documentation, freely available, continuously updated
```

### Special Cases

**No ISBN (older books):**
- Include Library of Congress number if available
- Note: "Pre-ISBN publication" in additional field

**Self-Published:**
- Publisher: Self-published or platform name (e.g., Leanpub)
- Include date of last known update if living document

**Translations:**
```markdown
### Original Title (German Edition)
Author: Original Author (Translated by Translator Name)
Original Year: YYYY
Translation Year: YYYY
...
```

---

## Academic Papers

### Required Fields
```markdown
### Paper Title: Subtitle if Present
Author: First Last, First Last, First Last
Year: YYYY (publication year)
Venue: Conference/Journal Full Name (Abbreviated Name)
DOI: 10.XXXX/...  (if available)
arXiv: XXXX.XXXXX (if available)
Link: https://direct-pdf-link.com or https://arxiv.org/abs/...
Description: One-sentence summary of main contribution
Why included: Significance and impact of the work
```

### Examples

**Conference Paper:**
```markdown
### Attention Is All You Need
Author: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
Year: 2017
Venue: Conference on Neural Information Processing Systems (NeurIPS 2017)
arXiv: 1706.03762
Link: https://arxiv.org/abs/1706.03762
Description: Introduces transformer architecture using self-attention mechanism, eliminating recurrence and convolution
Why included: Foundational work that revolutionized NLP and led to modern large language models
```

**Journal Paper:**
```markdown
### MapReduce: Simplified Data Processing on Large Clusters
Author: Jeffrey Dean, Sanjay Ghemawat
Year: 2004
Venue: Operating Systems Design and Implementation (OSDI 2004)
Published: Communications of the ACM, Vol. 51, No. 1
DOI: 10.1145/1327452.1327492
Link: https://research.google/pubs/pub62/
Description: Programming model and implementation for processing large datasets on commodity clusters
Why included: Seminal work that shaped big data processing paradigms, widely cited and implemented
```

**arXiv Preprint:**
```markdown
### Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
Author: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
Year: 2022
Venue: Conference on Neural Information Processing Systems (NeurIPS 2022)
arXiv: 2201.11903
Link: https://arxiv.org/abs/2201.11903
Description: Shows that prompting large language models to generate reasoning steps improves performance on complex tasks
Why included: Influential technique for improving LLM reasoning capabilities, widely adopted in practice
```

**Technical Report:**
```markdown
### The PageRank Citation Ranking: Bringing Order to the Web
Author: Lawrence Page, Sergey Brin, Rajeev Motwani, Terry Winograd
Year: 1999
Venue: Technical Report, Stanford InfoLab
Report Number: 1999-66
Link: http://ilpubs.stanford.edu:8090/422/
Description: Describes PageRank algorithm for ranking web pages based on link structure
Why included: Foundational algorithm behind Google Search, fundamental to web information retrieval
```

### Special Cases

**Multiple Versions:**
- Cite the published version if available
- Note preprint version in description if significant differences

**No DOI/arXiv:**
- Use direct PDF link from conference/journal site
- Include full bibliographic information

---

## Courses

### Required Fields
```markdown
### Course Title: Subtitle
Instructor: First Last (or Institution if multiple instructors)
Year: YYYY (year last updated or "Ongoing" if continuously updated)
Platform: Platform Name or "University Course"
Link: https://course-homepage.com
Duration: XX hours or "Self-paced" or "Semester-long"
Prerequisites: Required knowledge level
Description: What topics are covered and learning outcomes
Why included: What makes this course valuable
```

### Examples

**MOOC:**
```markdown
### Machine Learning Specialization
Instructor: Andrew Ng
Year: 2024
Platform: Coursera (Stanford University)
Link: https://www.coursera.org/specializations/machine-learning-introduction
Duration: 3 courses, approximately 3 months at 10 hours/week
Prerequisites: Basic Python programming, high school mathematics
Description: Covers supervised learning, unsupervised learning, and best practices with hands-on Python implementations
Why included: Industry-standard ML introduction, taught by field pioneer, widely recognized credential
```

**University Course (OpenCourseWare):**
```markdown
### Introduction to Algorithms
Instructor: Erik Demaine, Srini Devadas
Year: 2011
Platform: MIT OpenCourseWare
Link: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/
Duration: Semester-long, 24 lectures
Prerequisites: Programming experience, discrete mathematics
Description: Algorithmic thinking, algorithm design techniques, and complexity analysis with Python implementations
Why included: Gold-standard algorithms course, comprehensive coverage, high-quality lecture videos
```

**Interactive Tutorial Series:**
```markdown
### The Odin Project - Full Stack JavaScript
Instructor: The Odin Project Community
Year: 2024
Platform: The Odin Project
Link: https://www.theodinproject.com/paths/full-stack-javascript
Duration: 1000+ hours, self-paced
Prerequisites: None (starts from basics)
Description: Complete full-stack web development path including HTML, CSS, JavaScript, Node.js, React, and databases
Why included: Free, project-based, comprehensive curriculum with active community support
```

---

## Videos

### Required Fields
```markdown
### Video Title
Speaker: First Last (or Channel Name)
Year: YYYY
Venue: Conference Name / Channel Name / Platform
Duration: HH:MM:SS or "MM minutes"
Link: https://direct-video-link.com
Description: Brief summary of content and key points
Why included: Why this talk/video is valuable
```

### Examples

**Conference Talk:**
```markdown
### The Future of Programming
Speaker: Bret Victor
Year: 2013
Venue: Dropbox DBX Conference
Duration: 32 minutes
Link: https://www.youtube.com/watch?v=8pTEmbeENF4
Description: Historical perspective on programming paradigms and critique of current practices
Why included: Influential talk challenging programming assumptions, widely referenced in PL community
```

**Tutorial Series:**
```markdown
### But How Do It Know? - The Basic Principles of Computers
Speaker: Ben Eater
Year: 2024
Venue: YouTube Channel
Duration: Video series, varies
Link: https://www.youtube.com/c/BenEater
Description: Building an 8-bit computer from scratch on breadboards, explaining each component
Why included: Exceptional hands-on demonstration of computer architecture fundamentals
```

**Lecture:**
```markdown
### Dynamic Programming
Speaker: Erik Demaine
Year: 2011
Venue: MIT 6.006 Introduction to Algorithms
Duration: 49 minutes
Link: https://www.youtube.com/watch?v=OQ5jsbhAv_M
Description: Comprehensive introduction to dynamic programming with Fibonacci, shortest paths, and text justification examples
Why included: Clear explanation of complex topic by renowned algorithms researcher
```

---

## Interactive Resources

### Required Fields
```markdown
### Resource Title
Creator: Name or Organization
Year: YYYY
Platform: Where it's hosted
Link: https://direct-link.com
Type: Interactive tutorial / Playground / Notebook / Exercise set
Prerequisites: Required knowledge
Description: What skills are practiced and how
Why included: What makes this resource effective
```

### Examples

**Interactive Tutorial:**
```markdown
### Regex101
Creator: Firas Dib
Year: 2024
Platform: regex101.com
Link: https://regex101.com/
Type: Interactive regular expression tester and debugger
Prerequisites: Basic understanding of regex concepts
Description: Real-time regex testing with explanation of matches, multiple flavors support, community patterns library
Why included: Best-in-class regex development tool, immediate feedback, comprehensive documentation
```

**Coding Playground:**
```markdown
### Rust Playground
Creator: Rust Community
Year: 2024
Platform: play.rust-lang.org
Link: https://play.rust-lang.org/
Type: Online Rust compiler and execution environment
Prerequisites: Basic Rust syntax knowledge
Description: Compile and run Rust code in browser, share snippets, test different compiler versions
Why included: Official Rust playground, no installation required, essential for learning and sharing examples
```

---

## Documentation

### Required Fields
```markdown
### Documentation Title
Maintainer: Organization or Project Name
Year: YYYY (last major update) or "Living Document"
Type: Official Documentation / Specification / Reference / API Docs
Link: https://docs.example.com
Version: X.Y.Z (if applicable)
Description: What is documented and scope
Why included: Authority and usefulness
```

### Examples

**Official Documentation:**
```markdown
### Rust Reference
Maintainer: Rust Project
Year: Living Document
Type: Language Specification
Link: https://doc.rust-lang.org/reference/
Version: Current (tracks stable Rust)
Description: Formal specification of Rust language including grammar, semantics, and memory model
Why included: Authoritative language specification, required for compiler implementation
```

**API Documentation:**
```markdown
### PostgreSQL Documentation
Maintainer: PostgreSQL Global Development Group
Year: 2024
Type: Official Documentation
Link: https://www.postgresql.org/docs/current/
Version: 16.x
Description: Complete SQL reference, administration guide, internals documentation
Why included: Comprehensive, authoritative database documentation, covers all PostgreSQL features
```

---

## Tools

### Required Fields
```markdown
### Tool Name
Creator: Individual or Organization
Year: YYYY (first release) or range (YYYY-Present)
License: License Type
Platform: Operating Systems / Web / Cross-platform
Link: https://project-homepage.com or https://github.com/user/project
Language: Implementation language (if relevant)
Description: What the tool does and main features
Why included: Why this tool is notable
```

### Examples

**Software Tool:**
```markdown
### ripgrep
Creator: Andrew Gallant (BurntSushi)
Year: 2016-Present
License: MIT/Unlicense
Platform: Cross-platform (Linux, macOS, Windows)
Link: https://github.com/BurntSushi/ripgrep
Language: Rust
Description: Fast recursive grep-like search tool with automatic .gitignore handling and Unicode support
Why included: Fastest grep alternative, respects .gitignore by default, widely adopted replacement for grep/ag
```

**Library:**
```markdown
### PyTorch
Creator: Meta AI Research
Year: 2016-Present
License: BSD-3-Clause
Platform: Cross-platform
Link: https://pytorch.org/
Language: Python, C++, CUDA
Description: Open-source machine learning framework with dynamic computational graphs and extensive ecosystem
Why included: Industry-standard deep learning framework, research-friendly, large community
```

---

## Podcasts and Blogs

### Podcast Episodes
```markdown
### Episode Title
Podcast: Podcast Name
Host: First Last
Guest: First Last (if applicable)
Year: YYYY
Episode: Number or Date
Duration: MM minutes
Link: https://episode-link.com
Description: Topics discussed and key insights
Why included: Why this episode is valuable
```

### Blog Posts/Series
```markdown
### Blog Post Title
Author: First Last
Year: YYYY
Publication: Blog/Site Name
Link: https://full-article-url.com
Description: Main points and scope
Why included: Authority, insight, or influence
```

---

## Common Mistakes

**DON'T:**
- Use shortened URLs or redirects
- Omit required fields
- Use initials instead of full names (unless that's how they publish)
- Include marketing language in descriptions
- Copy descriptions from Amazon/marketing sites
- Use ISBN-10 when ISBN-13 available
- Link to paywalls when free versions exist

**DO:**
- Link to author's official site or repository
- Link to free legal versions (preprints, open-access)
- Include both DOI and open-access link when available
- Note if link requires institutional access
- Verify all information is current
- Use exact official titles

---

## Verification Checklist

Before submitting:

- [ ] All required fields present
- [ ] Link works and goes directly to resource
- [ ] Author names complete and correctly spelled
- [ ] Year is publication/update year, not access year
- [ ] ISBN/DOI/arXiv correct format
- [ ] Description is concise (one sentence)
- [ ] Justification explains specific value
- [ ] No marketing language or hyperbole
- [ ] Consistent with examples in this guide

---

Last Updated: 2025-11-19
