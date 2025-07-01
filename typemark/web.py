from flask import Flask, request, send_file, render_template_string, redirect, url_for
import os
import tempfile
from typemark import converter, themes

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    download_url = None
    if request.method == 'POST':
        file = request.files.get('markdown')
        theme = request.form.get('theme', 'vintage')
        format = request.form.get('format', 'pdf')
        notes = request.form.get('notes', '')
        watermark = request.form.get('watermark', '')
        doodles = request.form.getlist('doodles')
        custom_css = request.files.get('custom_css')
        
        if file:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.md', mode='w') as tmp_md:
                content = file.read().decode('utf-8')
                tmp_md.write(content)
                tmp_md_path = tmp_md.name
            
            # Handle custom CSS
            custom_css_path = None
            if custom_css:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.css', mode='w') as tmp_css:
                    css_content = custom_css.read().decode('utf-8')
                    tmp_css.write(css_content)
                    custom_css_path = tmp_css.name
            
            output_file = tmp_md_path + f'.{format}'
            try:
                converter.convert(
                    tmp_md_path, output_file, theme, format, 
                    notes if notes else None, 
                    doodles if doodles else None, 
                    watermark if watermark else None,
                    custom_css_path
                )
                download_url = url_for('download', filename=os.path.basename(output_file))
                message = 'Conversion successful!'
                # Move to static tmp dir for download
                static_dir = '/tmp/typemark_downloads'
                os.makedirs(static_dir, exist_ok=True)
                final_path = os.path.join(static_dir, os.path.basename(output_file))
                os.rename(output_file, final_path)
            except Exception as e:
                message = f'Conversion failed: {e}'
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>TypeMark Web UI</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                .form-group { margin-bottom: 15px; }
                label { display: block; margin-bottom: 5px; font-weight: bold; }
                input, select, textarea { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
                button { background: #007cba; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
                .checkbox-group { display: flex; gap: 10px; }
                .checkbox-group label { display: inline; }
                .message { padding: 10px; margin: 10px 0; border-radius: 4px; }
                .success { background: #d4edda; color: #155724; }
                .error { background: #f8d7da; color: #721c24; }
            </style>
        </head>
        <body>
            <h1>TypeMark Web UI</h1>
            <form method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label>Markdown File:</label>
                    <input type="file" name="markdown" accept=".md,.markdown" required>
                </div>
                
                <div class="form-group">
                    <label>Theme:</label>
                    <select name="theme">
                        {% for t in themes %}<option value="{{t}}">{{t}}</option>{% endfor %}
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Output Format:</label>
                    <select name="format">
                        <option value="pdf">PDF</option>
                        <option value="epub">EPUB</option>
                        <option value="docx">DOCX</option>
                        <option value="html">HTML</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Handwritten Notes:</label>
                    <textarea name="notes" placeholder="Add handwritten-style notes..."></textarea>
                </div>
                
                <div class="form-group">
                    <label>Margin Doodles:</label>
                    <div class="checkbox-group">
                        <label><input type="checkbox" name="doodles" value="star"> Star</label>
                        <label><input type="checkbox" name="doodles" value="arrow"> Arrow</label>
                        <label><input type="checkbox" name="doodles" value="heart"> Heart</label>
                        <label><input type="checkbox" name="doodles" value="check"> Check</label>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>Watermark:</label>
                    <input type="text" name="watermark" placeholder="Add watermark text...">
                </div>
                
                <div class="form-group">
                    <label>Custom CSS (optional):</label>
                    <input type="file" name="custom_css" accept=".css">
                </div>
                
                <button type="submit">Convert</button>
            </form>
            
            {% if message %}
            <div class="message {% if 'failed' in message %}error{% else %}success{% endif %}">
                {{message}}
            </div>
            {% endif %}
            
            {% if download_url %}
            <div class="form-group">
                <a href="{{download_url}}" class="button">Download {{format.upper()}}</a>
            </div>
            {% endif %}
        </body>
        </html>
    ''', message=message, download_url=download_url, themes=themes.list_themes(), format=request.form.get('format', 'pdf'))

@app.route('/download/<filename>')
def download(filename):
    static_dir = '/tmp/typemark_downloads'
    file_path = os.path.join(static_dir, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return f"File not found: {filename}", 404

if __name__ == '__main__':
    app.run(debug=True) 