# Project Summary: AI in Pedagogical Design and Delivery

## Overview

Complete workshop and companion website for building AI literacy among marketing and management faculty. Includes:
- Interactive 2-hour workshop with hands-on activities
- Companion website with resources and assessment tools
- Two-phase assessment strategy (reflective + diagnostic)
- Professional HTML/CSS website with responsive design
- All materials under CC BY 4.0 license

**Repository:** https://github.com/michaelborck-presentations/ai-in-pedagogical-design-and-delivery

---

## What's Included

### 1. Workshop Materials

**Main Presentation:**
- `ai-pedagogy-presentation.qmd` - 7-slide presentation (renders to PPTX/PDF/HTML)
- Duration: 2 hours
- Activities: 5 hands-on exercises

**Handouts & Guides:**
- `teaching-strategies-handout.md` - Implementation guide after workshop
- `ai-what-handout.md` - Quick reference for AI tools
- `references.md` - Bibliography and further reading

### 2. Resources (Pre-Reading Materials)

**Essential (Required for new users):**
- `what-to-expect.md` - Workshop overview and expectations (3 min)
- `quick-start-guide.md` - 5-minute essentials (5 min)

**Foundation (Recommended):**
- `what-is-ai.qmd` - AI concepts explained (10 min)
- `what-are-llms.qmd` - Large language models explained (12 min)

**Advanced (Optional):**
- `ai-in-pedagogical-design-and-delivery.md` - Pedagogy framework (8 min)
- `cognitive-prompting-in-education.md` - Prompting as pedagogy (7 min)
- `using-ai-in-education-roles-for-teaching-and-research.md` - AI roles (5 min)

**Total reading time:** 20-50 minutes (all optional)

### 3. Assessment Tools

**Diagnostic Quiz:**
- `website/content/assessment/ai-literacy-diagnostic.html`
- 15 interactive questions
- 4 adaptive profiles (Novice → Advanced)
- Instant personalized results
- Runs entirely offline
- Recommend: Day-of workshop (first 15 minutes)

**Reflective Profile:**
- Design using MS Forms (template in QUIZ-SETUP-GUIDE.md)
- 10 questions about concerns and motivations
- Personalized reading suggestions
- Recommend: Send 1 week before workshop

### 4. Companion Website

**Pages:**
- Landing page (index.html)
- Resources directory
- Materials directory
- Assessment hub with quiz
- Professional responsive design

**Architecture:**
- Pure HTML/CSS/JavaScript (no build process)
- 4 main pages + assessment quiz
- 60KB total size
- Mobile-friendly
- Sticky navigation
- Professional gradient theme

**Deployment:**
- Ready for GitHub Pages (from `docs/` folder)
- Auto-deploys on push
- Live URL: https://michaelborck-presentations.github.io/ai-in-pedagogical-design-and-delivery/

### 5. Documentation

**For Users:**
- `QUIZ-SETUP-GUIDE.md` - Complete quiz implementation manual
- `WEBSITE-BUILD-GUIDE.md` - Website build and deployment guide
- `WEBSITE-PLAN.md` - Architecture and strategy document
- `README.md` - Project overview

**For Developers:**
- `website/README.md` - Build instructions
- `website/content/assessment/README.md` - Quiz usage guide
- `.gitignore` - Configured for Quarto, website, and outputs

---

## File Structure

```
ai-in-pedagogical-design-and-delivery/
│
├── website/                           # Companion website source
│   ├── src/                          # Static website files
│   │   ├── index.html               # Landing page
│   │   ├── resources.html           # Resources directory
│   │   ├── materials.html           # Materials directory
│   │   ├── css/style.css            # Professional stylesheet
│   │   └── images/                  # Presentation visuals
│   │
│   ├── content/                      # Markdown source files
│   │   ├── resources/               # Pre-reading materials (7 files)
│   │   ├── materials/               # Presentation, handouts, refs
│   │   └── assessment/
│   │       ├── ai-literacy-diagnostic.html  # Interactive quiz
│   │       └── README.md
│   │
│   └── README.md                     # Development guide
│
├── docs/                             # GitHub Pages output (empty until built)
│
├── archive/                          # Deprecated files and research
│   ├── research-notes/              # Historical research
│   └── *.md files                   # Old documentation
│
├── ai-pedagogy-presentation.qmd     # Source presentation file
├── ai-pedagogy-presentation.pptx    # Generated PowerPoint
│
├── Documentation:
├── README.md                         # Main project documentation
├── WEBSITE-PLAN.md                   # Architecture and strategy
├── QUIZ-SETUP-GUIDE.md              # Assessment implementation
├── WEBSITE-BUILD-GUIDE.md           # Website build/deployment
├── PROJECT-SUMMARY.md               # This file
│
└── LICENSE                           # CC BY 4.0
```

---

## Quick Start for Different Users

### For Workshop Facilitators
1. Read `README.md` (project overview)
2. Review `ai-pedagogy-presentation.qmd` (main content)
3. Follow `QUIZ-SETUP-GUIDE.md` to set up assessments
4. Use `WEBSITE-BUILD-GUIDE.md` to deploy website locally
5. Share website URL with participants 1 week before

### For Participants
1. Optionally read pre-reading materials (20-50 min)
2. Take diagnostic quiz (15 min) on workshop day
3. Attend 2-hour workshop
4. Use `teaching-strategies-handout.md` for implementation

### For Developers/Customizers
1. Read `WEBSITE-PLAN.md` (understand architecture)
2. Read `WEBSITE-BUILD-GUIDE.md` (setup local dev)
3. Edit files in `website/src/` as needed
4. Test locally: `python -m http.server 8000`
5. Deploy to GitHub Pages

---

## Two-Phase Assessment Strategy

### Phase 1: Reflective Profile (Week Before)
- **Tool:** MS Forms (10 questions)
- **Purpose:** Surface anxieties, understand motivations
- **Output:** Personalized reading suggestions
- **Time:** 8-10 minutes

### Phase 2: Diagnostic Quiz (Day Of)
- **Tool:** Custom HTML/JavaScript
- **Purpose:** Measure AI literacy, personalize learning path
- **Output:** Instant adaptive profile + activity recommendations
- **Time:** 12-15 minutes
- **Features:** Offline, no backend, instant results

---

## Website Feature Highlights

### Design
- Clean, professional gradient theme (purple/indigo)
- Responsive layout (mobile to desktop)
- Card-based components for visual hierarchy
- Consistent typography and spacing

### Navigation
- Sticky header nav
- Breadcrumb navigation
- Footer with multiple link categories
- Internal linking throughout

### Components
- Hero section with CTA
- Feature cards
- Resource cards with metadata
- Alert boxes (info, success, warning)
- Buttons (primary, secondary, large)
- Badges and tags

### Accessibility
- Semantic HTML5
- Proper heading hierarchy
- Color contrast compliance
- Mobile-friendly touch targets

### Performance
- ~60KB total (HTML + CSS)
- No external dependencies
- Fast loading
- Works offline (after first load)

---

## Deployment Checklist

### Before Workshop

- [ ] Test diagnostic quiz locally
- [ ] Create MS Forms Reflective Profile
- [ ] Send Reflective Profile email 1 week prior
- [ ] Test website locally: `python -m http.server 8000`
- [ ] Copy website files to `docs/` folder
- [ ] Push to GitHub (auto-deploys to Pages)
- [ ] Verify live URL is accessible
- [ ] Share website URL with participants
- [ ] Print handouts if needed
- [ ] Test projection setup

### During Workshop

- [ ] Start local server for quiz: `python -m http.server 8000`
- [ ] Run quiz first thing (15 min)
- [ ] Reference participants' profiles during activities
- [ ] Note common themes from diagnostic results

### After Workshop

- [ ] Send results + personalized recommendations
- [ ] Include group insights (aggregate data)
- [ ] Share follow-up resources
- [ ] Optionally: Set up 3-month re-test

---

## Customization Guide

### Change Colors

Edit `/website/src/css/style.css`:
```css
--primary: #667eea;
--primary-dark: #764ba2;
--accent: #f59e0b;
```

### Update Content

Edit HTML files directly in `/website/src/`:
- `index.html` - Landing page
- `resources.html` - Resources list
- `materials.html` - Materials list

### Modify Quiz Questions

Edit `/website/content/assessment/ai-literacy-diagnostic.html`:
- Search for `<div class="question">`
- Edit questions, answers, scoring

### Customize Quiz Profiles

In same file, search for `const profiles = {`
- Edit profile names, descriptions
- Update activity recommendations
- Change reading suggestions

### Add New Pages

1. Create `website/src/newpage.html`
2. Copy structure from `index.html`
3. Update `<nav>` with new links
4. Add link to new page in other pages' nav

---

## Key Documents to Read

1. **README.md** - Start here for project overview
2. **QUIZ-SETUP-GUIDE.md** - If implementing assessments
3. **WEBSITE-BUILD-GUIDE.md** - If deploying or modifying website
4. **WEBSITE-PLAN.md** - If understanding architecture

---

## Technical Stack

**Frontend:**
- HTML5 (semantic markup)
- CSS3 (CSS Grid, Flexbox, Variables)
- Vanilla JavaScript (no frameworks)
- No external libraries or dependencies

**Build:**
- Quarto (for rendering presentation)
- Git (version control)
- GitHub Pages (hosting)

**Optional:**
- Python (local server)
- Node.js (alternative local server)
- VSCode (text editor)

---

## Support & Customization

### Getting Help

- Check `WEBSITE-BUILD-GUIDE.md` troubleshooting section
- Read relevant `.md` files for your use case
- Review comments in HTML/CSS files
- Email: michael.borck@curtin.edu.au

### Common Customizations

**Change workshop date/time:**
- Edit `website/src/index.html` (hero section)

**Change contact email:**
- Find and replace `michael.borck@curtin.edu.au` throughout

**Change institution:**
- Replace "Curtin University" in files
- Update footer and contact info

**Add custom resources:**
- Add links to `website/src/resources.html`
- Create new resource cards with metadata

**Rebrand:**
- Change CSS colors
- Update logo text (website/src/index.html)
- Modify footer content

---

## License & Attribution

**License:** CC BY 4.0 (Creative Commons Attribution)

**You can:**
- Use, adapt, remix, and share these materials
- Present the workshop yourself
- Modify for your context

**You must:**
- Attribute the original authors (Michael Borck & Curtin University)
- Keep the same license on derivatives

**Suggested attribution:**
> Materials adapted from "AI in Pedagogical Design and Delivery" by Michael Borck & Curtin University, licensed under CC BY 4.0

---

## Version History

**v1.0 (2025)** - Initial release
- Complete workshop materials
- Companion website
- Two-phase assessment system
- Documentation and guides

---

## Next Steps

1. **Review** - Read through README.md and QUIZ-SETUP-GUIDE.md
2. **Customize** - Edit website content for your context
3. **Test** - Run locally and verify all links work
4. **Deploy** - Push to GitHub Pages
5. **Share** - Send pre-reading email 1 week before workshop
6. **Present** - Run workshop with diagnostic quiz
7. **Follow-up** - Send results and personalized recommendations

---

## Questions?

- **Project:** michael.borck@curtin.edu.au
- **GitHub:** https://github.com/michaelborck-presentations/ai-in-pedagogical-design-and-delivery
- **Issues:** Use GitHub issues for bugs/suggestions
- **Contributions:** Pull requests welcome!

---

**Made with ❤️ for educators learning to teach with AI responsibly.**
