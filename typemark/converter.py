import os
import subprocess
from . import themes

class ConversionError(Exception):
    pass

def convert(input_md, output_file, theme, format='pdf', notes=None, doodles=None, watermark=None, custom_css=None):
    """
    Convert Markdown to the specified format (PDF, EPUB, DOCX, HTML).
    Applies theme, margin notes, doodles, and watermark if provided.
    """
    print(f"[TypeMark] Converting {input_md} to {output_file} as {format} with theme '{theme}'")
    
    # Get theme CSS path
    css_path = themes.get_theme_css_path(theme)
    if not os.path.exists(css_path):
        raise ConversionError(f"Theme CSS not found: {css_path}")
    
    # Handle custom CSS
    css_files = [css_path]
    if custom_css and os.path.exists(custom_css):
        css_files.append(custom_css)
        print(f"[TypeMark] Using custom CSS: {custom_css}")
    
    # Preprocess Markdown for notes and doodles
    pre_md = input_md
    if notes or doodles:
        pre_md = _preprocess_md(input_md, notes, doodles)
    
    # Prepare Pandoc command
    pandoc_cmd = [
        'pandoc', pre_md,
        '-o', output_file,
        '--standalone',
    ]
    if format != 'pdf':
        pandoc_cmd += ['-t', format]
    if format in ('pdf', 'html', 'epub'):
        for css_file in css_files:
            pandoc_cmd += [f'--css={css_file}']
    
    try:
        subprocess.run(pandoc_cmd, check=True, capture_output=True, text=True)
        print(f"[TypeMark] Conversion successful: {output_file}")
    except FileNotFoundError:
        if format == 'pdf':
            print("[TypeMark] Pandoc not found. Trying WeasyPrint for PDF...")
            try:
                from weasyprint import HTML, CSS
                stylesheets = [CSS(css_file) for css_file in css_files]
                HTML(pre_md).write_pdf(output_file, stylesheets=stylesheets)
                print(f"[TypeMark] PDF generated with WeasyPrint: {output_file}")
            except ImportError:
                raise ConversionError("Neither Pandoc nor WeasyPrint is available.")
        else:
            raise ConversionError("Pandoc is required for this export format.")
    except subprocess.CalledProcessError as e:
        raise ConversionError(f"Pandoc failed: {e.stderr}")
    
    # Watermark
    if watermark and format == 'pdf':
        add_watermark(output_file, watermark)

def _preprocess_md(input_md, notes, doodles):
    """Inject margin notes and doodles as HTML/CSS into a temp Markdown file."""
    import tempfile
    with open(input_md, 'r') as f:
        content = f.read()
    
    # Add notes as margin notes (using <aside> or custom span)
    if notes:
        content += f"\n\n<aside class='handwritten-note'>{notes}</aside>"
    
    # Add doodles as images in the margin
    if doodles:
        for doodle in doodles:
            content += f"\n\n<img src='doodles/{doodle}.svg' class='margin-doodle' />"
    
    # Write to temp file
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.md', mode='w')
    tmp.write(content)
    tmp.close()
    return tmp.name

def add_handwritten_notes(pdf_path, notes):
    """(No-op: handled in preprocess)"""
    pass

def add_margin_doodles(pdf_path, doodle_list):
    """(No-op: handled in preprocess)"""
    pass

def add_watermark(pdf_path, watermark_text):
    """Add a text watermark to each page of the PDF using PyPDF2."""
    try:
        from PyPDF2 import PdfReader, PdfWriter
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        import io
    except ImportError:
        print("[TypeMark] PyPDF2 and reportlab are required for watermarking.")
        return
    
    # Create watermark PDF in memory
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 40)
    can.setFillColorRGB(0.7, 0.7, 0.7, alpha=0.3)
    can.saveState()
    can.translate(300, 400)
    can.rotate(45)
    can.drawCentredString(0, 0, watermark_text)
    can.restoreState()
    can.save()
    packet.seek(0)
    
    watermark_pdf = PdfReader(packet)
    watermark_page = watermark_pdf.pages[0]
    
    # Read original PDF
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)
    
    # Write out watermarked PDF
    with open(pdf_path, 'wb') as f:
        writer.write(f)
    print(f"[TypeMark] Watermark added to {pdf_path}")

def export_to_format(input_md, output_file, format):
    """Export to EPUB, DOCX, or HTML using Pandoc."""
    if format not in ('epub', 'docx', 'html'):
        raise ConversionError(f"Unsupported export format: {format}")
    convert(input_md, output_file, theme='vintage', format=format)

def merge_css_files(css_files, output_file):
    """Merge multiple CSS files into one."""
    with open(output_file, 'w') as outfile:
        for css_file in css_files:
            if os.path.exists(css_file):
                with open(css_file, 'r') as infile:
                    outfile.write(f"/* {css_file} */\n")
                    outfile.write(infile.read())
                    outfile.write("\n\n")
    print(f"[TypeMark] Merged CSS files into: {output_file}") 