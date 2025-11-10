# Quiz Setup & Implementation Guide

This guide explains how to set up and use both assessment quizzes for your workshop.

## Two-Quiz Strategy

### 1. Reflective Profile Quiz (Week Before)
**Purpose:** Surface anxieties and motivations; personalise pre-reading  
**Platform:** MS Forms (your organisation)  
**Timing:** Send via email 1 week before workshop  
**Duration:** 8-10 minutes  
**Participant Action:** Complete optional form, receive profile + reading suggestions

**You need to create this in MS Forms with these 10 questions:**

```
Section 1: Mindset & Comfort
1. I feel confident trying new technology (5-point Likert)
2. AI will fundamentally change my teaching (5-point Likert)
3. Learning AI will take too much time (5-point Likert)

Section 2: Anxiety Signals  
4. Students using AI is cheating (5-point Likert)
5. AI will replace teachers (5-point Likert)
6. AI will make my expertise less valuable (5-point Likert)
7. AI outputs are too unreliable (5-point Likert)

Section 3: Values
8. What do you value most in teaching? (Multiple choice: knowledge / critical thinking / human connection / practical skills / all equally)
9. What's your biggest concern about AI? (Open text)
10. What would you like to learn? (Open text)
```

**Auto-Response Email Template:**

> Thanks for completing the Reflective Profile!
>
> **Your Profile: [Generated based on responses]**
>
> You're in the [Concerned/Curious/Enthusiastic] group. Here's what to expect:
>
> Pre-reading suggestions (2-3 specific files based on concerns):
> - what-is-ai.md if they worry about replacement
> - teaching-strategies-handout.md if they value human connection
> - quick-start-guide.md if they're time-pressed
>
> See you Thursday!

---

### 2. Diagnostic Quiz (Day Of)
**Purpose:** Measure AI literacy; provide real-time personalised guidance  
**Platform:** Custom HTML/JavaScript (included in repo)  
**Timing:** First 15 minutes of workshop  
**Duration:** 12-15 minutes  
**Output:** Instant adaptive profile + activity recommendations

**File:** `website/content/assessment/ai-literacy-diagnostic.html`

---

## Workshop Day Setup

### Before Participants Arrive

1. **Set up local server:**
   ```bash
   cd website
   python -m http.server 8000
   ```

2. **Test the quiz:**
   - Open browser to `http://localhost:8000/ai-literacy-diagnostic.html`
   - Take it yourself to verify it works
   - Check results display and recommendations

3. **Print results template (optional):**
   - Have blank cards or handouts for participants to write down their profile

### Opening (5 min)

**Introduce the diagnostic:**

> "Before we start, I want to understand where you're starting from so I can make this most useful for you. You'll spend 15 minutes on a quick assessment—not for grades, just to personalise your learning path. You'll get instant results with specific recommendations for what to focus on in our two hours together."

**Set expectations:**

> "Your results stay with you. They help us understand our group so we can adjust pacing. There are no wrong answers—we're just mapping AI literacy so we meet you where you are."

### During Quiz (15 min)

- Participants access quiz on laptops/tablets
- Tell them to minimise distractions (Slack, email, etc.)
- You watch aggregate responses if possible (optional: look at most common concerns)

### Immediately After (5 min)

- Participants review their profile and recommendations
- Optional: Ask volunteers to share their profile ("Who's a Novice Learner? Developing?")
- Reference profiles during activities:
  - "If you're a Novice, Activity 1 builds your foundation—take your time"
  - "If you're Proficient, Activity 3 will sharpen your critique skills"

---

## Creating the Reflective Profile Form (MS Forms)

### Steps

1. **Open MS Forms**
   - Go to `forms.office.com`
   - Create new form
   - Title: "AI Workshop: Reflective Profile"
   - Description: "Help us understand your starting point (optional, 8 min)"

2. **Add questions** (use the 10 listed above)
   - Likert scale: "Strongly Disagree → Strongly Agree" (5 points)
   - Multiple choice for values/concerns
   - Text for open responses

3. **Customize settings:**
   - Turn off "Collect respondent name" (optional responses)
   - Enable "One response per person" (optional; can skip if you want)
   - Randomize question order (optional; I'd keep order for coherence)

4. **Get the link:**
   - Click "Share" button
   - Copy link
   - Send via email with message

5. **Review responses:**
   - Set up auto-response in Forms
   - Review aggregate data before workshop (What concerns are most common?)

### Email Message to Send (Week Before)

Subject: **AI Workshop: Quick 8-minute Preparation**

> Hi everyone,
>
> Looking forward to seeing you [DATE] for "AI in Pedagogical Design and Delivery."
>
> Before we meet, I'd like to understand where you're starting from so I can make the workshop most useful for your group. This quick profile takes 8 minutes and helps me know what to emphasize.
>
> **[Link to MS Form]**
>
> After you complete it, you'll get suggestions for pre-reading based on your interests/concerns. Everything is optional—including pre-reading. But these resources are there if you want them:
>
> - what-to-expect.md (3 min overview)
> - quick-start-guide.md (5 min essentials)
> - what-is-ai.qmd & what-are-llms.qmd (20 min deep dive)
> - Plus others on the website
>
> See you soon!
> Michael

---

## During Workshop: Using Quiz Results

### Real-Time Adaptation

**Before Activity 1:**
> "Some of you are brand new to AI, some have used it. The first activity is designed for everyone, but there's no pace police—take what you need."

**Before Activity 2 (Prompting):**
> "This is where most of you identified growth opportunity. The CRAFT framework helps you move from 'okay' prompts to 'effective' prompts."

**Before Activity 4 (Assessment):**
> "Several of you marked 'student cheating' as your biggest concern. This activity directly addresses how to design assessments where AI use shows thinking, not hides it."

### Addressing Common Concerns

**If many selected "loss of human connection":**
- Emphasize: "AI handles the mechanics. You handle the meaningful interaction."
- Point to teaching-strategies-handout.md
- During activities, highlight human element

**If many selected "I don't have time":**
- Emphasize: "Start small. One task. 15 minutes."
- Point to quick-start-guide.md
- Share time-saving wins in activities

**If many are Novice:**
- Slow down on concepts
- Add examples
- Pair Novices with Developing participants for activities

---

## After Workshop: Follow-Up

### Send Results + Context (Within 1 Week)

Email template:

> **Your AI-Literacy Results**
>
> Here's your profile from the workshop diagnostic:
> - Knowledge: [X]% | Skills: [X]% | Confidence: [X]%
> - Profile: [Generated Name]
> - Activities we focused on: [List 2-3 based on their profile]
>
> **Group Insights** (aggregate, no individual names):
> - Most common concern: academic integrity
> - Average knowledge score: 55%
> - Most needed skill: prompt engineering
>
> **Next Steps:**
> - Try one "automate the tedious" task this month
> - Review recommended pre-reading
> - Email me with questions: [email]
>
> **In 3 Months:**
> - Re-take the diagnostic to measure progress
> - Share one success story (what worked in your class)

### Optional: 3-Month Check-In

Re-administer diagnostic (or short version) to measure:
- Did knowledge increase?
- Did confidence grow?
- Are people using AI (Yes/No)?
- What's working? What's not?

---

## Technical Notes

### Running the Diagnostic Locally

```bash
# Method 1: Python built-in server
cd website
python -m http.server 8000

# Method 2: Node http-server
npx http-server website

# Method 3: VS Code Live Server
# (Install extension, right-click file, "Open with Live Server")
```

Then access: `http://localhost:8000/ai-literacy-diagnostic.html`

### Data Collection (Optional)

The quiz runs 100% locally. If you want to collect results:

**Option 1: Manual (Simplest)**
- Ask participants to email results
- Or copy/paste results to a shared spreadsheet

**Option 2: Add Google Forms**
- Modify quiz to post results to a Google Form API
- (Requires JavaScript modification)

**Option 3: Simple Log File**
- Modify quiz to log results to a text file on server
- (Requires backend, not included)

---

## Tips for Success

✅ **Do:**
- Send Reflective Profile email exactly 1 week before (people forget if earlier)
- Have fun with the quiz language—make it feel safe, not evaluative
- Reference profiles throughout workshop to help people feel "seen"
- Follow up with personalised recommendations
- Use results to improve next iteration

❌ **Don't:**
- Rush through the quiz intro (people get anxious)
- Make it feel high-stakes ("This counts for something")
- Ignore the results (they cost you 15 min; use them!)
- Use results to label people ("Oh, you're the Novice group")

---

## Customization Ideas

**For future iterations:**
- Add discipline-specific questions (marketing vs. HR vs. academics)
- Ask about preferred learning style (visual/kinesthetic/auditory)
- Ask about specific use cases they want to try
- Add follow-up "What changed?" questions for re-test

**For different audiences:**
- For researchers: emphasize research applications (literature review, data analysis)
- For professional staff: emphasize efficiency/workflow
- For academics: emphasize pedagogy and student learning

