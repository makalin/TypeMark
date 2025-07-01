import os
from . import converter

def get_theme_css_path(theme_name):
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, '..', 'themes', f'{theme_name}.css')

def list_themes():
    """List available theme names."""
    themes_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'themes')
    return [f[:-4] for f in os.listdir(themes_dir) if f.endswith('.css')]

def preview_theme(theme_name, output_file='theme_preview.pdf', format='pdf'):
    """Generate a sample PDF or HTML preview for the given theme."""
    sample_md = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample.md')
    # Write a sample Markdown if not exists
    if not os.path.exists(sample_md):
        with open(sample_md, 'w') as f:
            f.write(f"""# Theme Preview\n\nThis is a preview of the **{theme_name}** theme.\n\n- Bullet\n- Points\n\n<aside class='handwritten-note'>Sample handwritten note!</aside>\n\n<img src='doodles/star.svg' class='margin-doodle' />\n""")
    try:
        converter.convert(sample_md, output_file, theme_name, format=format)
        print(f"[TypeMark] Theme preview generated: {output_file}")
    except Exception as e:
        print(f"[TypeMark] Theme preview failed: {e}") 