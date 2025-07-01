# TypeMark

**TypeMark** is a Python-powered tool that converts Markdown files into beautifully styled PDFs. It goes beyond basic formatting — bringing your documents to life with customizable themes, margin doodles, and handwritten note effects.

---

## 🚀 Features

* **Markdown → Aesthetic PDF**

  * Supports standard Markdown syntax
  * Converts to PDF via Pandoc or WeasyPrint

* **Customizable Themes**

  * Vintage typewriter
  * Futuristic neon
  * Minimalist clean

* **Handwritten Notes Effect**

  * Adds handwritten annotations or note-style comments in margins

* **Margin Doodles**

  * Decorative sketches (e.g. arrows, stars, paperclips)

* **CSS Styling**

  * Fully themeable via external CSS
  * Easy to add your own styles

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

---

## 📝 Usage

```bash
python typemark.py input.md --theme vintage --output myfile.pdf
```

---

## 🖌 Example Themes

| Theme              | Preview                                |
| ------------------ | -------------------------------------- |
| Vintage Typewriter | ![Vintage](assets/vintage_preview.png) |
| Futuristic Neon    | ![Neon](assets/neon_preview.png)       |
| Minimalist         | ![Minimal](assets/minimal_preview.png) |

---

## 🤝 Contributing

PRs are welcome! Submit your CSS themes, doodle packs, or feature ideas.

---

## 📜 License

MIT
