# Website Build & Deploy Guide

This guide covers how to build, preview, and deploy the companion website locally and to GitHub Pages.

## Quick Start

### View the Website Locally

```bash
# From project root
python -m http.server 8000

# Then open in browser:
# http://localhost:8000/website/src/index.html
```

That's it! The website is pure HTML/CSS/JavaScript. No build process needed.

---

## Project Structure

```
website/
├── src/                          # Static website files
│   ├── index.html               # Landing page
│   ├── resources.html           # Resources directory
│   ├── materials.html           # Materials directory
│   ├── css/
│   │   └── style.css            # Main stylesheet
│   └── images/                  # Presentation images
│
├── content/                      # Source markdown files (for reference)
│   ├── resources/               # Pre-reading materials
│   ├── materials/               # Presentation, handouts
│   └── assessment/
│       └── ai-literacy-diagnostic.html
│
└── README.md                     # Development documentation

docs/                            # OUTPUT (GitHub Pages)
├── index.html                   # (generated)
├── resources.html
├── materials.html
├── css/style.css
├── assessment/
│   └── ai-literacy-diagnostic.html
└── images/
```

---

## Local Development

### Prerequisites

- Python 3 or Node.js (for local server)
- Text editor (VSCode recommended)
- Modern web browser

### Running Locally

**Method 1: Python (Easiest)**
```bash
cd website/src
python -m http.server 8000

# Open: http://localhost:8000
```

**Method 2: Node.js**
```bash
cd website/src
npx http-server

# Open: http://localhost:8080
```

**Method 3: VSCode Live Server Extension**
1. Install "Live Server" extension
2. Right-click `website/src/index.html`
3. Select "Open with Live Server"

### Making Changes

**Editing HTML:**
- Edit `.html` files directly in `website/src/`
- Changes appear immediately when you refresh browser

**Editing CSS:**
- Edit `website/src/css/style.css`
- Refresh browser to see changes

**Adding New Pages:**
1. Create new `.html` file in `website/src/`
2. Copy structure from `index.html`
3. Update navigation links in header
4. Add link to page in other pages' navigation

### Testing Navigation

Test these paths:
- `/index.html` - Landing page
- `/resources.html` - Resources list
- `/materials.html` - Materials list
- `/assessment/ai-literacy-diagnostic.html` - Quiz
- `/css/style.css` - Stylesheet
- `/images/` - Presentation images

---

## Building for Deployment

The website is already "built" - it's just static files. But if you modify source markdown files in `website/content/`, you'd need to render them to HTML.

### If Using Quarto for Content Rendering

```bash
# From website/ directory
quarto render

# This converts markdown → HTML and outputs to ../docs/
```

Then deploy the `docs/` folder to GitHub Pages.

### Without Quarto

Just copy files directly:
```bash
# Copy everything from src/ to docs/
cp -r website/src/* docs/

# Then deploy docs/ to GitHub Pages
```

---

## Deployment to GitHub Pages

### Automatic Deployment (Recommended)

Your repo is already configured for GitHub Pages from `docs/` folder.

**To deploy:**

1. Copy website files to `docs/` folder:
```bash
cp -r website/src/* docs/
```

2. Commit and push:
```bash
git add docs/
git commit -m "Deploy website"
git push origin main
```

3. GitHub automatically publishes from `docs/` folder to:
   - https://michaelborck-presentations.github.io/ai-in-pedagogical-design-and-delivery/

### Checking Deployment Status

- Go to repo → Settings → Pages
- You'll see the live URL and deployment status
- If "Source" shows `docs/` and `main` branch, you're good to go

---

## Website Features

### Responsive Design
- Mobile-friendly (tested on phones, tablets, laptops)
- CSS Grid and Flexbox for layout
- Media queries for smaller screens

### Accessibility
- Semantic HTML5
- Proper heading hierarchy
- Color contrast meets WCAG standards
- Mobile-accessible navigation

### Performance
- No external dependencies
- Minimal CSS (~10KB)
- Images embedded directly
- Fast loading (< 1s on typical connection)

### Features
- Sticky navigation
- Gradient hero section
- Card-based layout
- CTA buttons
- Resource cards with metadata
- Footer with links
- Breadcrumb navigation

---

## Customization

### Change Colors

Edit CSS variables in `website/src/css/style.css`:

```css
:root {
    --primary: #667eea;          /* Main color */
    --primary-dark: #764ba2;     /* Darker shade */
    --accent: #f59e0b;           /* Accent color */
    --text-dark: #1f2937;        /* Text color */
    --text-light: #6b7280;       /* Secondary text */
    --bg-light: #f9fafb;         /* Light background */
}
```

Then save and refresh browser.

### Change Content

Edit HTML files directly:
- `website/src/index.html` - Main landing page
- `website/src/resources.html` - Resources list
- `website/src/materials.html` - Materials list

### Add New Section

1. Create `website/src/new-page.html`
2. Copy HTML structure from `index.html`
3. Modify content in `<section>` tags
4. Add navigation link in `<nav>` section
5. Save and test locally

### Embed Videos or Other Media

Add to HTML:
```html
<iframe width="560" height="315" 
  src="https://www.youtube.com/embed/VIDEO_ID" 
  frameborder="0" allowfullscreen></iframe>
```

---

## Troubleshooting

### Pages not loading
- Check file paths in links (relative to `website/src/`)
- Ensure files are in correct folder
- Check browser console for errors (F12)

### Styles not applying
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
- Check CSS file is in `website/src/css/style.css`
- Verify `<link>` tag points to correct path

### Images not showing
- Images should be in `website/src/images/`
- Use relative paths: `../images/filename.png`
- Check image file extensions (.png, .jpg, etc.)

### Links broken
- Use relative paths for internal links
- Root should be `website/src/`
- Example: `resources.html` or `assessment/ai-literacy-diagnostic.html`

---

## SEO & Metadata

Each page has:
- Unique `<title>` tag (appears in browser tab)
- `<meta description>` (appears in search results)
- Proper heading hierarchy (h1, h2, h3)
- Semantic HTML (nav, section, footer, etc.)

To improve SEO:
1. Update title and description for new pages
2. Use descriptive anchor text for links
3. Add alt text to images (if any)
4. Keep heading hierarchy logical

---

## File Size & Optimization

Current website:
- CSS: ~10 KB
- HTML (all pages): ~50 KB
- Total: ~60 KB (very lightweight)

No optimization needed, but if you want to reduce further:
- Minify CSS: `css-minify` tool or online minifier
- Remove unused CSS: Rarely needed here

---

## Backup & Version Control

All website files are in git:
```bash
git log --oneline website/src/  # See all website changes
git diff website/src/           # See what changed
git restore website/src/        # Undo changes
```

To revert to previous version:
```bash
git checkout COMMIT_HASH website/src/
git commit -m "Revert website to previous version"
```

---

## Next Steps

1. **Test locally** - Make sure it looks good
2. **Customize** - Update colors, text, links as needed
3. **Deploy** - Copy to `docs/` and push to GitHub
4. **Share** - Send the GitHub Pages URL to participants

Your live website will be at:
```
https://michaelborck-presentations.github.io/ai-in-pedagogical-design-and-delivery/
```

---

## Questions?

- GitHub issues: Report bugs or suggest improvements
- Email: michael.borck@curtin.edu.au
- Edit files directly - it's just HTML/CSS!
