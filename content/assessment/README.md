# Assessment Tools

## AI-Literacy Diagnostic Quiz

**File:** `ai-literacy-diagnostic.html`

### What It Is
An interactive, self-contained HTML/JavaScript quiz that assesses AI literacy across three dimensions:
- **Knowledge:** Understanding of AI capabilities and limitations
- **Skills:** Practical prompting and critique abilities
- **Confidence:** Self-reported confidence using AI in teaching

### When to Use
**Timing:** First 15 minutes of the workshop (or on arrival)

Participants complete the quiz individually, receive instant results with personalized guidance, and use those recommendations to focus their workshop engagement.

### How It Works

1. **Quiz Structure (15 questions)**
   - Section 1: Knowledge (5 multiple-choice questions)
   - Section 2: Skills (5 questions: 4 MC + 1 confidence scale)
   - Section 3: Attitudes (5 questions: 2 MC + 2 Likert scales + 1 open)

2. **Scoring**
   - Knowledge: 0-100% (multiple choice only)
   - Skills: 0-100% (multiple choice only)
   - Confidence: 0-100% (average of 2 Likert scales)

3. **Results Display**
   - Three-part score visualization
   - Adaptive profile (Novice → Developing → Proficient → Advanced)
   - Activity recommendations specific to their profile
   - Pre-reading suggestions

### Using the Quiz

#### Opening Statement
You might introduce it as:

> "This 15-minute assessment helps personalize your learning. You're not being graded—we're just understanding where you're starting so we can focus on what's most useful for you. Your results stay with you."

#### During the Quiz
- Run locally (no internet needed)
- Use Quarto preview or simple HTTP server: `python -m http.server 8000`
- Participants access: `http://localhost:8000/ai-literacy-diagnostic.html`

#### Processing Results
Participants get instant personalized guidance:
- If Novice skills: "Activity 2 will level up your prompting significantly"
- If proficient knowledge but low confidence: "Your understanding is solid; practice will build confidence"
- If concerned about cheating: "Activity 4 directly addresses assessment design with AI"

### Customizing the Quiz

To modify questions or profiles, edit the HTML file:

**Questions:** Look for `<div class="question">` blocks (easily editable)

**Profiles:** Search for `const profiles = {` and modify profile names, descriptions, activities, and readings

**Scoring:** Modify the `calculateResults()` function to change how scores are calculated

### Technical Details

- **No Backend:** Runs entirely in browser; no data collection
- **No External Dependencies:** Pure HTML/CSS/JavaScript
- **Offline Compatible:** Works without internet connection
- **Export:** Results can be copied to clipboard
- **Responsive:** Works on laptops and tablets

### Example Output

A "Developing AI Practitioner" would see:
```
Knowledge: 60% | Skills: 40% | Confidence: 70%

Profile: Developing AI Practitioner
You understand some AI concepts and you're curious to build practical 
skills. You're past the "what is AI?" stage and ready to get hands-on 
with real applications.

Workshop Recommendations:
→ Activity 2 (The Art of the Prompt - CRAFT)
  Focus here—CRAFT framework will level up your prompting significantly
→ Activity 3 (5-Step Critique)
  Build confidence in evaluating outputs—spend time here

Pre-Reading Focus:
→ what-are-llms.qmd (refresh your knowledge)
→ teaching-strategies-handout.md (integration ideas)
```

### Follow-Up

After workshop, send results + facilitator notes:
- Aggregate feedback ("Most common concern was academic integrity")
- Personalized recommendations for continued learning
- Link to "next steps" resources on website

---

## Notes on Assessment Approach

**Why This Assessment?**

This quiz serves multiple purposes:
1. **Scaffolding:** Personalizes workshop pacing and focus
2. **Self-awareness:** Helps participants understand their starting point
3. **Documentation:** Gives facilitators insight into audience
4. **Benchmarking:** Optional re-test 6 months later to measure progress

**Not a Pass/Fail:**

Emphasis that this is diagnostic, not evaluative. There are no "right" answers—it's about understanding their current literacy so we can meet them where they are.

**How It Frames the Workshop:**

- Novices: "We're building your foundation"
- Developing: "We're leveling up your skills"
- Proficient: "We're refining your strategic thinking"
- Advanced: "We're deepening your practice and leadership"
