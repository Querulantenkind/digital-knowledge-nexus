# Governance

This document describes how decisions are made in Digital Knowledge Nexus.

---

## Philosophy

**Self-Organizing Through Rules**

Digital Knowledge Nexus is designed to minimize governance needs:
- Clear, objective rules replace subjective decisions
- Templates enforce consistency
- Community reviews contributions
- Minimal central authority needed

**When governance is needed:**
- Structural changes (new domains, major reorganizations)
- Policy changes (contribution rules, quality criteria)
- Conflict resolution
- Security issues

---

## Decision-Making Levels

### Level 1: Automatic (No Discussion Needed)

**Examples:**
- Adding resources following templates
- Fixing broken links
- Correcting typos
- Updating outdated information

**Process:**
1. Submit pull request
2. Automated checks pass
3. Community member reviews
4. Merge

**Timeline:** 2-7 days

---

### Level 2: Community Discussion (Normal Issues)

**Examples:**
- Category placement disputes
- Quality criteria interpretation
- New subcategories
- Template adjustments

**Process:**
1. Open issue with proposal
2. Community discusses (minimum 7 days)
3. Consensus or maintainer decision
4. Implement

**Timeline:** 1-4 weeks

**Consensus:** 
- No strong objections after discussion period
- Majority support from active participants
- Addresses raised concerns

---

### Level 3: Structural Changes (Major Proposals)

**Examples:**
- New domains (01-13, etc.)
- Domain reorganization
- Format file changes
- Major policy changes

**Process:**
1. Open RFC (Request for Comments) issue
2. Detailed proposal with rationale
3. Discussion period (minimum 30 days)
4. Community feedback incorporated
5. Final proposal
6. Maintainer decision with community input
7. Implementation plan
8. Migration guide if needed

**Timeline:** 2-6 months

**Requirements:**
- Clear problem statement
- Detailed solution
- Impact analysis
- Migration plan
- Community support

---

## Roles

### Contributors
**Anyone who submits a pull request**

**Responsibilities:**
- Follow CONTRIBUTING.md
- Respond to review feedback
- Follow CODE_OF_CONDUCT.md

**Rights:**
- Submit contributions
- Participate in discussions
- Vote (informally) on proposals

**Become a contributor:** Submit your first PR

---

### Active Contributors
**Regular contributors with multiple merged PRs**

**Additional Responsibilities:**
- Help review others' contributions
- Answer questions from newcomers
- Provide feedback on proposals

**Additional Rights:**
- Weighted input on discussions
- Can propose structural changes
- Can request fast-track for routine changes

**Become an active contributor:** 10+ merged PRs over 6+ months

---

### Maintainers
**Trusted community members with merge access**

**Responsibilities:**
- Review and merge pull requests
- Enforce contribution guidelines
- Make final decisions on disputes
- Maintain repository health
- Respond to security issues
- Guide community discussions

**Rights:**
- Merge pull requests
- Close invalid issues
- Make policy decisions (with community input)
- Repository administration access

**Become a maintainer:** 
- Invited by existing maintainers
- Demonstrated judgment and technical skill
- Active contributor for 1+ year
- Community trust and support

**Current Maintainers:** See MAINTAINERS.md

---

### Emeritus Maintainers
**Former maintainers who stepped down**

**Status:**
- Retain commit access (optional)
- Advisory role
- Recognition for contributions

**Transition:**
- Voluntary step-down
- Inactivity (6+ months)
- Removal for cause (Code of Conduct violations)

---

## Decision Making

### Routine Decisions
**Handled by:** Any maintainer

**Examples:**
- Merging standard contributions
- Fixing obvious errors
- Routine maintenance

**Process:** Single maintainer approval

---

### Policy Decisions
**Handled by:** Maintainers with community input

**Examples:**
- Quality criteria changes
- Contribution rule changes
- Template updates

**Process:**
1. Discussion issue (7+ days)
2. Community feedback
3. Maintainer consensus
4. Implementation

**Consensus:** Majority of active maintainers, no strong objections

---

### Structural Decisions
**Handled by:** Maintainers with strong community consensus

**Examples:**
- New domains
- Major reorganizations
- Format changes

**Process:**
1. RFC issue (30+ days)
2. Extensive community discussion
3. Maintainer review
4. Community polling (informal)
5. Final decision
6. Implementation plan

**Requirements:**
- Strong community support
- No viable alternatives
- Clear improvement over status quo
- Feasible implementation

---

### Emergency Decisions
**Handled by:** Any maintainer

**Examples:**
- Security issues
- Malicious content
- Code of Conduct violations
- Repository compromise

**Process:**
1. Immediate action if needed
2. Notify other maintainers
3. Document decision
4. Community notification

**Review:** Post-action review within 7 days

---

## Conflict Resolution

### Step 1: Discussion
Most conflicts resolved through civil discussion:
- Listen to all perspectives
- Assume good faith
- Focus on what's best for users
- Refer to documented policies

### Step 2: Mediation
If discussion stalls:
- Request maintainer mediation
- Present all viewpoints
- Maintainer facilitates resolution
- Document decision and rationale

### Step 3: Maintainer Decision
If mediation fails:
- Maintainers make final decision
- Based on:
  - Project goals
  - User needs
  - Technical merit
  - Community feedback
- Decision is documented
- Decision is binding

### Step 4: Appeal
- Can appeal to full maintainer team
- New information or circumstances
- Single appeal allowed
- Final decision stands

---

## Proposal Process

### Small Changes
**Use:** Standard issue or PR

**Template:**
```markdown
## What
Brief description

## Why
Justification

## How
Implementation approach
```

---

### Medium Changes
**Use:** Discussion issue

**Template:**
```markdown
## Summary
One paragraph overview

## Problem
What needs to change and why

## Proposal
Detailed solution

## Alternatives
Other options considered

## Impact
Who/what is affected

## Implementation
Steps to implement
```

**Timeline:** 1-4 weeks

---

### Major Changes (RFC)
**Use:** RFC (Request for Comments) issue

**Template:**
```markdown
## Title
Clear, descriptive title

## Summary
One paragraph overview

## Motivation
Why is this needed?
What problems does it solve?

## Detailed Design
Complete specification of change
Examples and edge cases

## Drawbacks
Potential problems or concerns

## Alternatives
Other approaches considered
Why rejected

## Migration Plan
How to transition from current state
Breaking changes and mitigation

## Impact Analysis
- Contributors: How are they affected?
- Users: How are they affected?
- Maintenance: Ongoing impact
- Other: Additional considerations

## Timeline
Proposed implementation schedule

## Open Questions
Unresolved issues for discussion
```

**Timeline:** 2-6 months

---

## Removing Content

### Individual Resources
**Reasons:**
- Permanently dead link
- Malicious content
- Copyright violation
- Security concern
- Duplicate entry

**Process:**
1. Open issue with evidence
2. Community/maintainer review
3. Decision within 7 days
4. Document in commit message

---

### Categories
**Reasons:**
- Obsolete technology (and historical value minimal)
- Duplicate of another category
- Consistent lack of resources

**Process:**
1. RFC with migration plan
2. 30-day discussion
3. Maintainer decision
4. Redirect to replacement
5. Document in CHANGELOG.md

---

## Adding Maintainers

**Process:**
1. Existing maintainer nominates
2. Nominee must:
   - Accept nomination
   - Confirm time commitment
   - Agree to responsibilities
3. Current maintainers discuss (private)
4. Consensus required (all maintainers)
5. Public announcement
6. Onboarding period (30 days)

**Criteria:**
- Technical expertise
- Good judgment
- Community respect
- Availability
- Alignment with project values

---

## Removing Maintainers

### Voluntary
- Maintainer announces intent
- Transition period (30 days recommended)
- Handoff of responsibilities
- Status change to Emeritus

### Inactivity
- 6+ months no activity
- Private outreach by maintainers
- If no response: move to Emeritus
- Can return if becomes active

### For Cause
**Grounds:**
- Code of Conduct violations
- Abuse of position
- Malicious actions
- Security breaches

**Process:**
1. Private discussion among maintainers
2. Evidence gathered
3. Accused maintainer notified
4. Opportunity to respond
5. Maintainer vote (75% required for removal)
6. Access removed immediately if vote passes
7. Public announcement with minimal details
8. Appeal process available

---

## Amending Governance

**When:** Governance process itself needs change

**Process:**
1. RFC issue proposing changes
2. 30-day minimum discussion
3. Maintainer consensus required
4. Document in CHANGELOG.md
5. Update GOVERNANCE.md

**Requires:**
- Strong justification
- Community support
- Maintainer consensus

---

## Transparency

### Public
- All technical decisions
- Policy discussions
- Structural changes
- Most conflicts

### Private
- Security issues (until resolved)
- Maintainer nominations
- Removals for cause
- Personal conflicts
- Code of Conduct investigations

**Private discussions documented (without sensitive details) after resolution**

---

## Project Values

**Decision-making guided by:**

1. **User First**
   - What benefits users most?
   - Ease of use and navigation
   - Quality over quantity

2. **Contributor Friendly**
   - Clear rules reduce friction
   - Templates make contribution easy
   - Feedback is constructive

3. **Community Driven**
   - Decisions reflect community needs
   - No single person controls direction
   - Distributed authority

4. **Sustainable**
   - Minimal ongoing maintenance
   - Self-organizing where possible
   - Clear processes

5. **Inclusive**
   - Welcoming to all backgrounds
   - Multiple learning styles supported
   - Accessible content

---

## Getting Help

**Questions about governance:**
- Open a Question issue
- Ask in discussion thread
- Contact maintainers directly (for sensitive matters)

**Propose governance changes:**
- Open RFC issue
- Explain problem and solution
- Engage with feedback

---

Last Updated: 2025-11-19
Version: 1.0.0