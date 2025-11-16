# Companion Website: Architecture & Quiz Strategy

## Website Technology Stack

**Recommendation: HTML + Quarto Hybrid (NOT Pure Quarto)**

### Why?
- **Quarto alone:** Academic look, limited design control
- **Pure HTML:** Too much manual work for content updates
- **Hybrid:** Best of both—professional design + easy content management

### How It Works
1. Quarto renders markdown → plain HTML content (no styling)
2. Custom HTML templates & CSS create professional look
3. JavaScript handles interactivity (navigation, quiz logic)
4. Result: Polished site that's easy to maintain

---

## File Structure (After Reorganization)

```
website/                              # SOURCE files
├── src/
│   ├── index.html                   # Landing page (cards, nav)
│   ├── templates/
│   │   ├── page-template.html       # Wrapper for all pages
│   │   └── quiz-results.html        # Quiz results display
│   ├── css/
│   │   └── style.css                # Professional theme
│   ├── js/
│   │   ├── nav.js                   # Navigation logic
│   │   ├── quiz.js                  # Quiz engine + routing
│   │   └── utils.js                 # Helpers
│   └── images/
│       ├── logo.png
│       ├── favicon.ico
│       └── icons/
│
├── content/                          # Markdown source files
│   ├── resources/                    # (renamed from pre-readings)
│   │   ├── what-to-expect.md
│   │   ├── quick-start-guide.md
│   │   ├── what-is-ai.md
│   │   ├── what-are-llms.md
│   │   ├── ai-in-pedagogical-design-and-delivery.md
│   │   ├── cognitive-prompting-in-education.md
│   │   └── using-ai-in-education.md
│   │
│   ├── materials/
│   │   ├── presentation.md
│   │   ├── handout-ai-tools.md
│   │   ├── handout-teaching-strategies.md
│   │   └── references.md
│   │
│   └── assessment/
│       └── ai-literacy-quiz.html    # Interactive quiz (custom)
│
├── _quarto.yml                       # Minimal Quarto config (just render settings)
├── build.sh                          # Build script
└── README.md                         # How to build locally

docs/                                 # OUTPUT (GitHub Pages)
├── index.html                        # (generated)
├── resources/
│   ├── what-to-expect.html
│   ├── quick-start-guide.html
│   └── ...
├── materials/
│   ├── presentation.html
│   ├── presentation.pdf
│   └── ...
├── assessment/
│   └── ai-literacy-quiz.html
├── css/
│   └── style.css
├── js/
│   └── quiz.js
└── images/
```

---

## Two-Phase Assessment Strategy

### PHASE 1: Reflective Profile (Week Before)

**What it is:** Quick self-assessment to surface anxieties & motivations  
**When:** Sent 1 week before workshop via email link  
**Duration:** 8-10 minutes  
**Purpose:** Help YOU understand audience, help them frame learning

**Questions (10 items):**

**Mindset & Comfort (3 Qs)**
- "I feel confident trying new technology"
- "AI will fundamentally change my teaching"
- "Learning AI will take time I don't have"

**Anxiety Signals (4 Qs)**
- "Students using AI is cheating"
- "AI will replace teachers"
- "AI will make my expertise less valuable"
- "AI outputs are too unreliable"

**Values (3 Qs)**
- "What do you value most?" (knowledge / critical thinking / human connection / practical skills)
- "Biggest concern about AI?" (open text)
- "What do you want to learn?" (open text)

**Output:** Not a score, but a **reflective profile**

```
YOUR REFLECTIVE PROFILE
═══════════════════════

Confidence: [░░░▓░░░░] (Cautious)

You're in the "Thoughtful Skeptic" group:
✓ Interested in AI but concerned about implications
✓ Values human connection highly
✓ Worried about workload

What we'll emphasize:
• How AI enhances (not replaces) teaching
• Time-saving, not time-adding
• Keeping the human element central
• Ethical frameworks

Pre-reading suggestion:
→ what-is-ai.md (builds understanding)
→ quick-start-guide.md (practical)
```

**Implementation:** Google Form or Typeform (embedded on website)
- Free, simple, auto-emails results
- Optional: aggregate responses show you patterns

---

### PHASE 2: Diagnostic Quiz (During Workshop)

**What it is:** Interactive assessment measuring current AI literacy  
**When:** First 15 minutes of workshop (or on arrival)  
**Duration:** 12-15 minutes  
**Purpose:** Personalise workshop recommendations in real-time

**Structure (15 questions):**

**Knowledge: What AI Can/Can't Do (5 Qs)**
- Multiple choice questions testing understanding of capabilities
- Scenarios: "AI gave you X answer, what's the problem?"
- Examples: hallucinations, outdated knowledge, bias

**Skills: Prompting & Critique (5 Qs)**
- "Which prompt is better?" (compare two)
- "What's wrong with this AI output?" (identify issues)
- Practical scenarios they'll see in workshop

**Attitudes: Concerns & Priorities (5 Qs)**
- "What concerns you most?" (academic integrity / connection / bias / privacy)
- Likert-scale: "I'm worried AI will replace my job"
- Open-ended: What do you hope to learn?

**Instant Results → Adaptive Guidance:**

```
YOUR AI-LITERACY PROFILE
════════════════════════

Knowledge:   ████░░░░░░ 40% (Developing)
Prompting:   ███░░░░░░░ 30% (Novice)
Confidence:  ███████░░░ 70% (Good!)

PERSONALISED WORKSHOP PATH:
───────────────────────────

Activity 1 (Automate the Tedious):
→ YOU: Essential foundation - we'll start here

Activity 2 (Art of the Prompt - CRAFT):
→ YOU: This is where you'll get big wins - lean in!

Activity 3 (5-Step Critique):
→ YOU: Critical skill for you - spend extra time here

Activity 4 (Assessment Stress-Test):
→ YOU: Your concern about cheating will be addressed

Pre-reading focus:
1. what-are-llms.md (understand limitations)
2. teaching-strategies-handout.md (your human-connection concern)

Questions? You're in "Developing Knowledge" group - facilitators will 
provide extra support. Raise your hand anytime!
```

**Implementation:** Custom HTML/JavaScript quiz
- Runs entirely in browser (no backend needed)
- Instant results with guidance text
- Can export results to CSV for your records

---

## Integration Timeline

### 1 Week Before Workshop
- Email: Reflective Profile link + info sheet
- Participant completes (8 min)
- Receives personalised profile + reading suggestions
- They choose what to read based on their results

### Day Of (First 15 minutes)
1. Participants arrive, access Diagnostic Quiz (via link/laptop)
2. Complete quiz (12-15 min)
3. Get instant personalised guidance card
4. Facilitator can adjust pacing/emphasis based on aggregate results

### During Workshop
- Facilitator references groups: "Novices, Activity 1 builds your foundation..."
- Adaptive timing: If group scores low on prompting, spend more time on CRAFT

### After Workshop
- Results + facilitator notes emailed to each participant
- Recommended "next steps" reading
- Link to practice resources

---

## Technology Choices

### Reflective Profile (Week Before)
**Option 1: Google Form** (Easiest)
- Free, auto-emails results
- Basic design but functional
- No backend needed

**Option 2: Typeform** (Better UX)
- Professional look
- Better user experience
- Free tier allows ~10 questions
- Can auto-email personalised results

### Diagnostic Quiz (During Workshop)
**Custom HTML/JavaScript** (Best Control)
- Runs offline (no internet dependency during workshop)
- Instant results, personalised guidance
- Easy to modify questions
- Can log results to email or spreadsheet
- Professional look (matches your website)

---

## Building Locally

Create `website/build.sh`:

```bash
#!/bin/bash

# Render markdown to HTML (plain, no styling)
quarto render content/*.md --to html
quarto render content/materials/*.md --to html

# Render presentation to multiple formats
quarto render content/materials/presentation.md --to pptx
quarto render content/materials/presentation.md --to pdf
quarto render content/materials/presentation.md --to html

# Copy everything to docs/
cp -r src/* docs/
cp -r content/* docs/resources/
cp -r content/materials/* docs/materials/
cp -r content/assessment/* docs/assessment/

echo "✓ Site built to docs/"
echo "✓ Run: python -m http.server 8000 (then visit http://localhost:8000)"
```

Run locally:
```bash
cd website
./build.sh
python -m http.server 8000
# Visit http://localhost:8000
```

---

## .gitignore Updates

Keep generated files in `docs/` so GitHub Pages works:

```
# Quarto build artifacts (don't commit)
/.quarto/
*_files/
*_cache/

# But DO commit docs/ output (for GitHub Pages)
!docs/
!docs/**/*.html
!docs/**/*.pdf
!docs/**/*.css
!docs/**/*.js
!docs/**/*.json

# Don't commit temp build files
website/.build/
website/*.tmp
```

---

## Next Steps

1. **Decide on quiz approach:**
   - Use Google Form for Reflective? (simpler)
   - Build custom HTML for Diagnostic? (more control)

2. **Choose landing page style:**
   - Cards + navigation (modern)
   - Timeline/process flow (storytelling)
   - Simple nav + featured resources (minimal)

3. **Start with file structure:**
   - Rename `pre-readings/` → `resources/`
   - Create `website/src/`, `website/content/` folders
   - Move relevant files

4. **Create minimal HTML template** (I can draft)

Would you like me to start building the custom HTML template, or do you want to finalise the structure first?
