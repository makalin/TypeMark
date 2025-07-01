import argparse
import sys
from . import converter, themes

def main():
    parser = argparse.ArgumentParser(description='TypeMark: Markdown to Aesthetic PDF')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Convert command
    convert_parser = subparsers.add_parser('convert', help='Convert Markdown to PDF/EPUB/DOCX/HTML')
    convert_parser.add_argument('input', help='Input Markdown file')
    convert_parser.add_argument('--output', '-o', default='output.pdf', help='Output file')
    convert_parser.add_argument('--theme', '-t', default='vintage', help='Theme name')
    convert_parser.add_argument('--format', '-f', choices=['pdf', 'epub', 'docx', 'html'], default='pdf', help='Output format')
    convert_parser.add_argument('--notes', '-n', help='Add handwritten notes')
    convert_parser.add_argument('--doodles', '-d', nargs='+', help='Add margin doodles')
    convert_parser.add_argument('--watermark', '-w', help='Add watermark text')
    
    # List themes command
    list_parser = subparsers.add_parser('themes', help='List available themes')
    
    # Preview theme command
    preview_parser = subparsers.add_parser('preview', help='Preview a theme')
    preview_parser.add_argument('theme', help='Theme name to preview')
    preview_parser.add_argument('--output', '-o', default='theme_preview.pdf', help='Output file')
    preview_parser.add_argument('--format', '-f', choices=['pdf', 'html'], default='pdf', help='Preview format')
    
    # Web UI command
    web_parser = subparsers.add_parser('web', help='Start web UI')
    web_parser.add_argument('--host', default='127.0.0.1', help='Host to bind to')
    web_parser.add_argument('--port', type=int, default=5000, help='Port to bind to')
    
    args = parser.parse_args()
    
    if args.command == 'convert':
        try:
            converter.convert(args.input, args.output, args.theme, args.format, args.notes, args.doodles, args.watermark)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == 'themes':
        themes_list = themes.list_themes()
        print("Available themes:")
        for theme in themes_list:
            print(f"  - {theme}")
    elif args.command == 'preview':
        try:
            themes.preview_theme(args.theme, args.output, args.format)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == 'web':
        from . import web
        print(f"Starting web UI at http://{args.host}:{args.port}")
        web.app.run(host=args.host, port=args.port)
    else:
        parser.print_help()

if __name__ == '__main__':
    main() 