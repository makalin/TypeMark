# TypeMark

**TypeMark** is a Python-powered tool that converts Markdown files into beautifully styled PDFs. It goes beyond basic formatting — bringing your documents to life with customizable themes, margin doodles, and handwritten note effects.

---

## 🚀 Features

* **Markdown → Aesthetic PDF**
  * Supports standard Markdown syntax
  * Converts to PDF via Pandoc or WeasyPrint
  * Multi-format export (EPUB, DOCX, HTML)

* **Customizable Themes**
  * Vintage typewriter
  * Futuristic neon
  * Minimalist clean
  * Custom CSS support

* **Handwritten Notes Effect**
  * Adds handwritten annotations or note-style comments in margins

* **Margin Doodles**
  * Decorative sketches (stars, arrows, hearts, checkmarks)
  * SVG-based doodles for crisp rendering

* **Advanced Features**
  * Text watermarks
  * Custom CSS injection
  * Web UI for easy conversion
  * Theme preview system

---

## 💡 Addon Ideas

* **Interactive Theme Editor**

  * Web-based interface to create new PDF themes visually

* **AI Doodle Generator**

  * Uses a small model (or connects to an API) to generate margin doodles based on document context

* **Watermark / Signature**

  * Add personal watermarks or digital signatures

* **Multi-format Export**

  * Output to EPUB, DOCX, or HTML along with PDF

* **Template Packs**

  * Downloadable community-contributed templates (e.g. academic paper, zine style)

---

## ⚙️ Tech Stack

* Python
* Pandoc or WeasyPrint
* CSS for themes
* Optional: Flask (for future web UI)

---

## 📦 Installation

```bash
git clone https://github.com/makalin/typemark.git
cd typemark
pip install -r requirements.txt
```

**Dependencies:**
- Pandoc (for conversion)
- WeasyPrint (PDF fallback)
- PyPDF2 + reportlab (watermarking)

---

## 📝 Usage

### Command Line Interface

**Basic conversion:**
```bash
python -m typemark convert input.md --theme vintage --output myfile.pdf
```

**With all features:**
```bash
python -m typemark convert input.md \
  --theme neon \
  --format pdf \
  --notes "Important note here" \
  --doodles star arrow heart \
  --watermark "CONFIDENTIAL" \
  --output document.pdf
```

**List available themes:**
```bash
python -m typemark themes
```

**Preview a theme:**
```bash
python -m typemark preview vintage --format html
```

**Start web UI:**
```bash
python -m typemark web --host 0.0.0.0 --port 8080
```

### Web Interface

Start the web UI and visit `http://localhost:5000` for a browser-based interface with:
- File upload
- Theme selection
- Format options (PDF, EPUB, DOCX, HTML)
- Handwritten notes
- Margin doodles
- Watermarks
- Custom CSS upload

### Python API

```python
from typemark import converter, themes

# Convert with theme
converter.convert('input.md', 'output.pdf', 'vintage')

# Convert with all features
converter.convert(
    'input.md', 'output.pdf', 'neon',
    notes="Important note",
    doodles=['star', 'arrow'],
    watermark="DRAFT"
)

# List themes
print(themes.list_themes())

# Preview theme
themes.preview_theme('minimal', 'preview.pdf')
```

---

## 🖌 Example Themes

| Theme              | Preview                                |
| ------------------ | -------------------------------------- |
| Vintage Typewriter | ![Vintage](assets/vintage_preview.png) |
| Futuristic Neon    | ![Neon](assets/neon_preview.png)       |
| Minimalist         | ![Minimal](assets/minimal_preview.png) |

---

## 🎨 Customization

### Custom CSS
```bash
python -m typemark convert input.md --theme vintage --custom-css mystyle.css
```

### Custom Doodles
Add SVG files to the `doodles/` directory and reference them in your Markdown:
```markdown
<img src="doodles/my-doodle.svg" class="margin-doodle" />
```

---

## 🤝 Contributing

PRs are welcome! Submit your:
- CSS themes
- Doodle packs
- Feature ideas
- Bug reports

---

## 📜 License

MIT
