# Website Build Instructions

This directory contains the source files for the companion website.

## Structure

```
website/
├── src/                    # Static HTML, CSS, JS, images
├── content/                # Markdown source files
│   ├── resources/         # Pre-reading materials
│   ├── materials/         # Presentation, handouts, references
│   └── assessment/        # Quiz HTML/JS
└── _quarto.yml           # Quarto render config
```

## Building Locally

### Prerequisites
- [Quarto](https://quarto.org/docs/get-started/) installed
- Python 3 (for local server)

### Steps

1. **Render markdown to HTML:**
   ```bash
   cd website
   quarto render
   ```

2. **Preview locally:**
   ```bash
   python -m http.server 8000
   # Visit http://localhost:8000/docs
   ```

3. **Build presentation in multiple formats:**
   ```bash
   quarto render content/materials/presentation.qmd --to pptx
   quarto render content/materials/presentation.qmd --to pdf
   quarto render content/materials/presentation.qmd --to html
   ```

## Output

All rendered files go to `../docs/` (GitHub Pages root)

## Deployment

Push to GitHub:
```bash
git add .
git commit -m "Update website content"
git push origin main
```

GitHub Pages automatically deploys from the `docs/` folder.
