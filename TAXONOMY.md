# Taxonomy and Categorization Philosophy

This document explains the organizational principles behind Digital Knowledge Nexus's structure and provides guidance for categorization decisions.

---

## Core Principles

### 1. Hierarchical Depth
**Target: 3-5 levels deep**
```
Level 1: Domain (01-12)
Level 2: Major Category
Level 3: Subcategory
Level 4: Specific Topic
Level 5: Subtopic (when needed)
```

**Rationale:**
- Shallow (1-2 levels): Too broad, hard to navigate
- Deep (3-5 levels): Precise placement, good organization
- Too deep (6+ levels): Diminishing returns, maintenance burden

### 2. Separation of Concerns
**Topic vs Format**

Each topic area has 8 format files:
- books.md
- papers.md
- courses.md
- videos.md
- interactive.md
- documentation.md
- tools.md
- podcasts-blogs.md

**Why separate by format?**
- Users have learning style preferences
- Different formats serve different needs
- Prevents file bloat
- Makes contribution straightforward

### 3. Technology-Neutral Organization
**Organize by concept, not implementation**

Good:
```
/machine-learning/supervised-learning/
/databases/relational/
/networking/protocols/
```

Avoid:
```
/python-ml/  (technology-specific)
/postgres/   (should be under relational databases)
/tcp-ip-for-windows/  (platform-specific)
```

**Exception:** When technology defines the category
```
/programming-languages/python/  ✓
/cloud-computing/aws/  ✓
/databases/relational/postgresql/  ✓
```

### 4. Stable Structure
**Categories should be:**
- Long-lasting (not tied to trends)
- Broadly applicable
- Conceptually clear
- Mutually exclusive where possible

---

## Domain Organization

### 01 - FUNDAMENTALS
**Purpose:** Theory and mathematical foundations

**Includes:**
- Computer science theory
- Mathematics for computing
- Electrical engineering fundamentals
- Physics for computing

**Rationale:** These topics underpin everything else. Pure theory before application.

**Boundary cases:**
- Applied algorithms → 01-FUNDAMENTALS (theory) vs 02-SOFTWARE-ENGINEERING (implementation)
- Rule: If it's about proving correctness → FUNDAMENTALS. If it's about writing code → SOFTWARE-ENGINEERING

---

### 02 - SOFTWARE ENGINEERING
**Purpose:** Software development practices and tools

**Includes:**
- Programming languages
- Software architecture
- Development methodologies
- Testing and quality
- DevOps

**Rationale:** Building and maintaining software systems.

**Boundary cases:**
- Systems programming vs embedded → Language-focused = SOFTWARE-ENGINEERING. Hardware-focused = HARDWARE
- Web frameworks → WEB-DEVELOPMENT. General frameworks → SOFTWARE-ENGINEERING

---

### 03 - HARDWARE
**Purpose:** Physical computing systems and digital design

**Includes:**
- Digital design (FPGA, ASIC)
- Computer architecture
- Embedded systems
- PCB design
- Hardware security

**Rationale:** Below the software abstraction layer.

**Boundary cases:**
- Embedded Linux → HARDWARE (hardware-centric). Linux kernel → SYSTEMS (OS-centric)
- GPU programming → SOFTWARE-ENGINEERING (programming). GPU architecture → HARDWARE (design)

---

### 04 - ARTIFICIAL INTELLIGENCE
**Purpose:** Machine learning and AI systems

**Includes:**
- Machine learning algorithms
- Deep learning
- NLP, computer vision
- ML frameworks
- MLOps

**Rationale:** Large, rapidly growing field deserves dedicated domain.

**Boundary cases:**
- Statistical learning → FUNDAMENTALS (theory) vs AI (application)
- Data analysis → DATA-SCIENCE. ML modeling → AI
- AI theory → AI (kept together for coherence)

---

### 05 - SYSTEMS
**Purpose:** System software and infrastructure

**Includes:**
- Operating systems
- Distributed systems
- Databases
- Networking
- Cloud computing

**Rationale:** System-level software that applications build on.

**Boundary cases:**
- Web servers → SYSTEMS (infrastructure) vs WEB-DEVELOPMENT (application)
- Container orchestration → SYSTEMS (infrastructure level)

---

### 06 - SECURITY
**Purpose:** Cybersecurity and information security

**Includes:**
- Cryptography
- Application security
- Network security
- Penetration testing
- Blockchain (crypto focus)

**Rationale:** Cross-cutting concern deserving dedicated space.

**Boundary cases:**
- Secure coding → SECURITY. Software architecture → SOFTWARE-ENGINEERING
- Hardware security → HARDWARE. Crypto implementations → SECURITY

---

### 07 - DATA SCIENCE
**Purpose:** Data analysis and processing

**Includes:**
- Data analysis
- Visualization
- Big data systems
- Data engineering

**Rationale:** Distinct from AI (not necessarily ML) and databases (not just storage).

**Boundary cases:**
- ML model training → AI. Data preparation → DATA-SCIENCE
- Database design → SYSTEMS. Data modeling → DATA-SCIENCE

---

### 08 - WEB DEVELOPMENT
**Purpose:** Web application development

**Includes:**
- Frontend frameworks
- Backend frameworks
- Full-stack development
- Web security

**Rationale:** Large, specialized domain with distinct tooling.

**Boundary cases:**
- API design → SOFTWARE-ENGINEERING (general) vs WEB-DEVELOPMENT (web-specific)
- HTTP protocol → SYSTEMS. HTTP/2 usage in web apps → WEB-DEVELOPMENT

---

### 09 - MOBILE DEVELOPMENT
**Purpose:** Mobile application development

**Includes:**
- Android development
- iOS development
- Cross-platform frameworks
- Mobile-specific patterns

**Rationale:** Platform-specific concerns and tooling.

**Boundary cases:**
- Mobile UI patterns → MOBILE. General UI patterns → SOFTWARE-ENGINEERING
- Mobile networking → MOBILE (mobile-specific). Networking → SYSTEMS

---

### 10 - GAME DEVELOPMENT
**Purpose:** Video game creation

**Includes:**
- Game engines
- Graphics programming
- Game design
- Physics simulation

**Rationale:** Specialized domain with unique constraints and tools.

**Boundary cases:**
- Game physics → GAME-DEVELOPMENT. Physics simulation (general) → SPECIALIZED-DOMAINS
- 3D rendering → GAME-DEVELOPMENT (games) or SPECIALIZED-DOMAINS (general graphics)

---

### 11 - SPECIALIZED DOMAINS
**Purpose:** Emerging or niche technical domains

**Includes:**
- Quantum computing
- Robotics
- Computer graphics (non-game)
- Computational biology
- IoT
- Edge computing

**Rationale:** Important but don't fit cleanly elsewhere.

**Growth path:** Topics here may become domains if they grow large enough.

**Boundary cases:**
- IoT firmware → HARDWARE. IoT platforms → SPECIALIZED-DOMAINS
- Robotics control → SPECIALIZED-DOMAINS. Control theory → FUNDAMENTALS

---

### 12 - META SKILLS
**Purpose:** Skills for effective technical work

**Includes:**
- Software craftsmanship
- System design
- Technical writing
- Learning methods
- Career development

**Rationale:** Process and professional development.

**Boundary cases:**
- Code review → META-SKILLS (process). Code quality → SOFTWARE-ENGINEERING (technical)
- Technical writing → META-SKILLS. Documentation tools → SOFTWARE-ENGINEERING

---

## Categorization Decision Framework

### Step 1: Identify Primary Focus
Ask: "What is this resource PRIMARILY about?"

**Example: "Deep Learning for Computer Vision"**
- Deep learning? → AI
- Computer vision? → AI
- Both equally? → Choose more specific

**Answer:** 04-ARTIFICIAL-INTELLIGENCE/computer-vision/

### Step 2: Navigate the Hierarchy
From domain, drill down:
```
04-ARTIFICIAL-INTELLIGENCE/
  └── computer-vision/
      └── [What specific aspect?]
          ├── image-classification/
          ├── object-detection/
          ├── segmentation/
          └── ...
```

### Step 3: Choose Most Specific Applicable Category
Don't stop too early:
```
❌ 04-ARTIFICIAL-INTELLIGENCE/
❌ 04-ARTIFICIAL-INTELLIGENCE/computer-vision/
✓ 04-ARTIFICIAL-INTELLIGENCE/computer-vision/object-detection/
```

### Step 4: Select Format
Based on resource type, not content complexity.

---

## Common Categorization Challenges

### Challenge 1: Multiple Equally Relevant Topics

**Example:** "Network Security Protocols"
- Could go in: SECURITY/network-security/
- Could go in: SYSTEMS/networking/protocols/

**Resolution:**
1. Which is more specific? (Equal)
2. Which is the resource's perspective? (Security perspective)
3. Place in: SECURITY/network-security/

**Rule:** Choose the perspective of the resource, not all possible applications.

### Challenge 2: Cross-Cutting Concerns

**Example:** "Machine Learning for Embedded Systems"
- AI topic: Machine learning
- Hardware context: Embedded systems

**Resolution:**
1. What is being taught? (ML techniques)
2. What is the context? (Embedded systems)
3. Place in: 04-ARTIFICIAL-INTELLIGENCE/mlops/ or 04-ARTIFICIAL-INTELLIGENCE/ml-frameworks/
4. Note embedded context in description

**Rule:** Categorize by what is taught, note context in description.

### Challenge 3: Historical vs Modern

**Example:** "Assembly Language Programming"
- Historical: FUNDAMENTALS?
- Practical: SOFTWARE-ENGINEERING?

**Resolution:**
Place in: 02-SOFTWARE-ENGINEERING/programming-languages/
**Rationale:** Still practical for embedded/performance-critical work

**Rule:** If still used practically → appropriate domain. If purely historical → FUNDAMENTALS if theoretical significance.

### Challenge 4: Tool vs Concept

**Example:** "Docker"
- Container technology concept
- Specific tool

**Resolution:**
Place in: 02-SOFTWARE-ENGINEERING/devops/containerization/docker/
**Rationale:** Tool gets subcategory under concept

**Pattern:**
```
/concept/
  ├── [general resources about concept]
  └── specific-tool/
      └── [tool-specific resources]
```

### Challenge 5: Language-Specific Topics

**Example:** "Python Machine Learning Libraries"
- Python resources?
- Machine learning resources?

**Resolution:**
Place in: 04-ARTIFICIAL-INTELLIGENCE/ml-frameworks-libraries/
Note Python in description

**Alternative if very Python-specific:**
02-SOFTWARE-ENGINEERING/programming-languages/application-languages/python/
With note about ML focus

**Rule:** Categorize by domain (ML), note language unless resource is primarily about the language itself.

---

## Naming Conventions

### Folder Names
- lowercase
- hyphens-for-spaces
- descriptive-not-abbreviated
- singular for concepts (machine-learning not machine-learnings)
- plural for collections (frameworks, tools, languages)

**Good:**
```
machine-learning
programming-languages
web-development
```

**Bad:**
```
ML  (too abbreviated)
Machine_Learning  (underscores)
machine learning  (spaces)
MachineLearning  (camelCase)
```

### Category Names
Use established terminology:
- "Machine Learning" not "ML" (in documentation)
- "Natural Language Processing" not "NLP" (first mention)
- "Application Programming Interface" → "API" is acceptable (widely used)

---

## Evolution and Growth

### When to Add New Categories

**Good reasons:**
- 10+ resources with no good existing category
- Established field deserving dedicated space
- Prevents artificial splitting of resources
- Community consensus

**Bad reasons:**
- Single resource needs a home (use existing)
- Trending topic (may be temporary)
- Personal preference for organization
- Company-specific technology

### When to Split Categories

**Indicators:**
- 50+ resources in a single category
- Clear natural subdivision exists
- Different learning paths within category
- Maintenance becoming difficult

**Process:**
1. Propose split in issue
2. Show clear subdivision
3. Provide migration plan
4. Get community feedback
5. Implement with redirects

### When to Merge Categories

**Indicators:**
- Consistently fewer than 5 resources
- Unclear boundaries with sibling categories
- Duplicate or overlapping content
- Difficult to categorize between them

**Process:**
1. Propose merge in issue
2. Show overlap and confusion
3. Identify target category
4. Get community feedback
5. Implement with redirects

---

## Category Relationships

### Hierarchical Relationships
Parent → Child relationships are strict:
```
programming-languages/
  └── systems-programming/
      └── rust/
```

Rust is a systems programming language, which is a programming language.

### Cross-References (Conceptual Only)
Don't create links, but acknowledge relationships:

**Related categories:**
- SECURITY/cryptography/ ↔ FUNDAMENTALS/mathematics/number-theory/
- AI/deep-learning/ ↔ FUNDAMENTALS/mathematics/linear-algebra/
- HARDWARE/computer-architecture/ ↔ SOFTWARE-ENGINEERING/programming-languages/

**Handle via:**
- Mention in descriptions
- Cross-topic resources note relationships
- Index shows full structure

---

## Special Cases

### Deprecated Technologies
- Include if historically significant
- Mark as CLASSIC
- Note modern alternatives

### Emerging Technologies
- Wait for stability (6+ months)
- Require substantial resources
- Place in SPECIALIZED-DOMAINS initially
- Can promote to domain if grows

### Vendor-Specific
- Include under appropriate category
- Don't create vendor-specific domains
- Example: AWS under cloud-computing, not separate domain

### Interdisciplinary Topics
- Choose primary discipline
- Note others in description
- Example: "Bioinformatics" → SPECIALIZED-DOMAINS/computational-biology/

---

## Anti-Patterns

### Don't: Create Tool-Specific Top Levels
```
❌ /react/
✓ /web-development/frontend/frameworks/react/
```

### Don't: Organize by Difficulty
```
❌ /beginner/machine-learning/
✓ /artificial-intelligence/machine-learning/
   (with BEGINNER section inside)
```

### Don't: Organize by Format at High Level
```
❌ /books/programming/
✓ /software-engineering/programming-fundamentals/books.md
```

### Don't: Create Company-Specific Categories
```
❌ /google/
✓ Multiple categories (TensorFlow in AI, Go in languages, etc.)
```

### Don't: Create Trend-Based Categories
```
❌ /web3/
✓ Blockchain in SECURITY, distributed systems in SYSTEMS
```

---

## Decision Tree
```
Is this a resource about digital technology?
  No → Not suitable for repository
  Yes ↓

What is the primary domain? (01-12)
  → Choose most specific applicable domain
  
What is the main category within domain?
  → Navigate hierarchy
  
What is the specific topic?
  → Go as deep as structure allows
  
What format is the resource?
  → Choose one of 8 format files
  
What difficulty level?
  → Place in appropriate section
```

---

## Getting Help with Categorization

**If unsure:**
1. Check INDEX.md for similar resources
2. Search existing content for patterns
3. Open a Question issue
4. Ask in Category Request

**Provide:**
- Resource details
- Your reasoning
- Alternative placements considered
- Why you're unsure

**Community will help determine best placement.**

---

## Future Considerations

### Potential New Domains (Not Yet Warranted)
- Blockchain (currently in SECURITY)
- DevOps (currently in SOFTWARE-ENGINEERING)
- Cloud Native (currently in SYSTEMS/DEVOPS)

**Criteria for promotion:**
- 500+ resources
- Clear, stable boundaries
- Distinct tooling and community
- Long-term relevance established

### Potential Restructuring
None planned, but if needed:
- Major version bump
- Migration guide
- Backward compatibility period
- Community discussion

---

Last Updated: 2025-11-19