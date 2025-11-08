# Rendering Guide: QMD to HTML/PDF

This guide covers how to render all the `.qmd` files to HTML and PDF for deployment.

## Quick Start

```bash
cd website
quarto render
```

That's it! Quarto will:
- Render all `.qmd` files in `content/` to HTML and PDF
- Output to `../docs/` folder
- Create standalone HTML files (with embedded CSS/resources)
- Generate PDF versions
- Generate PowerPoint presentation
- Copy resources (images) as needed

## Before You Render

### Prerequisites

1. **Install Quarto** (if not already installed)
   ```bash
   # macOS
   brew install quarto
   
   # Or download from: https://quarto.org/docs/get-started/
   ```

2. **Verify installation**
   ```bash
   quarto --version
   ```

## What Gets Rendered

### `.qmd` Files → HTML + PDF

**Resources (pre-reading materials):**
- `website/content/resources/what-is-ai.qmd` → `docs/what-is-ai.html` + `docs/what-is-ai.pdf`
- `website/content/resources/what-are-llms.qmd` → `docs/what-are-llms.html` + `docs/what-are-llms.pdf`
- `website/content/resources/quick-start-guide.qmd` → `docs/quick-start-guide.html` + `docs/quick-start-guide.pdf`
- `website/content/resources/what-to-expect.qmd` → `docs/what-to-expect.html` + `docs/what-to-expect.pdf`
- `website/content/resources/ai-in-pedagogical-design-and-delivery.qmd` → `docs/ai-in-pedagogical-design-and-delivery.html` + `.pdf`
- `website/content/resources/cognitive-prompting-in-education.qmd` → `docs/cognitive-prompting-in-education.html` + `.pdf`
- `website/content/resources/using-ai-in-education-roles-for-teaching-and-research.qmd` → `docs/using-ai-in-education-roles-for-teaching-and-research.html` + `.pdf`

**Materials (handouts, presentation, references):**
- `website/content/materials/teaching-strategies-handout.qmd` → HTML + PDF
- `website/content/materials/references.qmd` → HTML + PDF
- `website/content/materials/presentation.qmd` → HTML + PDF + **PPTX**

### Assessment (already HTML)
- `website/content/assessment/ai-literacy-diagnostic.html` → (copied to docs/)

### Static Website (copied as-is)
- `website/src/index.html` → `docs/index.html`
- `website/src/resources.html` → `docs/resources.html`
- `website/src/materials.html` → `docs/materials.html`
- `website/src/css/style.css` → `docs/css/style.css`
- `website/src/images/` → `docs/images/`

## Render Output Features

### HTML Files
- **Standalone:** All CSS and resources embedded (one file = complete)
- **Table of Contents:** Auto-generated from headings
- **Responsive:** Works on mobile and desktop
- **Searchable:** Can search within the page
- **Printable:** Print-friendly styling

### PDF Files
- **Professional:** Formatted for printing
- **Navigation:** Table of contents with clickable links
- **Color-coded:** Headings and links in color
- **Metadata:** Title, author, date in document properties

### PowerPoint (PPTX)
- **Presentation-ready:** Use for live presenting
- **Slide per section:** Each top-level heading = one slide
- **Images embedded:** All presentation images included
- **Editable:** Customize in PowerPoint/Google Slides as needed

## Quarto Configuration

The rendering is configured in `website/_quarto.yml`:

```yaml
project:
  type: default
  output-dir: ../docs          # Output to docs/
  resources:
    - src/images/              # Include images

render:
  - content/**/*.qmd           # Render all .qmd files

format:
  html:
    embed-resources: true      # Standalone HTML files
    toc: true                  # Table of contents
    embed-resources: true
    css: src/css/style.css     # Use website CSS
  
  pdf:
    toc: true                  # PDF also has TOC
    colorlinks: true           # Colored links in PDF

execute:
  freeze: auto                 # Cache execution results
```

## Before Rendering

Check that:
1. All `.qmd` files have YAML front matter (between `---` lines)
2. Image paths in presentation are correct: `../src/images/filename.png`
3. No syntax errors in `.qmd` files

## Rendering Commands

### Render everything
```bash
cd website
quarto render
```

### Render a specific file
```bash
cd website
quarto render content/resources/what-is-ai.qmd
```

### Render to specific format
```bash
cd website
quarto render content/materials/presentation.qmd --to html
quarto render content/materials/presentation.qmd --to pdf
quarto render content/materials/presentation.qmd --to pptx
```

### Preview in browser while editing
```bash
cd website
quarto preview
```

Then open: http://localhost:4949

## After Rendering

### Check the output
```bash
ls -la docs/
```

You should see:
- `*.html` files (standalone HTML)
- `*.pdf` files (PDFs)
- `presentation.pptx` (PowerPoint)
- `css/style.css` (copied)
- `images/` folder (copied)
- Static HTML pages

### Test the links
1. Open `docs/index.html` in browser
2. Click "Resources" → all links should work
3. Click "Materials" → all links should work
4. Try downloading PDFs

### Deploy to GitHub Pages
```bash
git add docs/
git commit -m "Render QMD files to HTML and PDF"
git push origin main
```

GitHub Pages auto-deploys from `docs/` folder.

## Troubleshooting

### "command not found: quarto"
- Install Quarto: `brew install quarto` (or download from quarto.org)
- Or use full path: `/usr/local/bin/quarto render`

### Images not showing in rendered HTML
- Check image paths in .qmd files (should be `../src/images/filename.png`)
- Verify images exist in `website/src/images/`
- Make sure `_quarto.yml` includes `resources: - src/images/`

### Links broken in rendered HTML
- Links in `website/src/resources.html` and `website/src/materials.html` should point to `../filename.html`
- These files point to the rendered output in `docs/`

### PDF generation failing
- Install a PDF rendering engine: `quarto install tinytex`
- Or use Quarto's built-in PDF support

### PPTX presentation looking wrong
- Check that image paths use `../src/images/` format
- Use `![](path/to/image.png)` syntax (not HTML img tags)
- Each top-level `#` heading becomes one slide

## Common Issues

### Changed a .qmd but it didn't update
- Quarto caches results; use `quarto render --no-cache`

### Want to rebuild everything from scratch
```bash
rm -rf docs/
quarto render
```

### Different output wanted for different formats
Use format-specific YAML in the front matter:

```yaml
format:
  html:
    embed-resources: true
    toc: true
  pdf:
    toc: false
    margin-left: 1in
  pptx:
    footer: "Your footer here"
```

## Workflow

1. **Edit .qmd file** → Make changes in `website/content/`
2. **Render** → `quarto render`
3. **Preview** → Open rendered HTML in browser
4. **Deploy** → `git add docs/` and push to GitHub
5. **Visit live site** → https://michaelborck-presentations.github.io/...

## Tips

- Use `quarto preview` while editing for live reload
- Use `quarto render --watch` to auto-render on file changes
- Keep `.qmd` files in `website/content/`, not `website/src/`
- Static HTML pages (index.html, resources.html, etc.) go in `website/src/`
- Let Quarto handle the rendering; don't edit rendered HTML files directly

## Questions?

See `WEBSITE-BUILD-GUIDE.md` for more details on the build process.
