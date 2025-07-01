import unittest
import os
from typemark import converter

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.sample_md = os.path.join(os.path.dirname(__file__), '../typemark/sample.md')
        if not os.path.exists(self.sample_md):
            with open(self.sample_md, 'w') as f:
                f.write("# Test\n\nThis is a test document.\n")

    def test_convert_pdf(self):
        out = 'test_out.pdf'
        converter.convert(self.sample_md, out, 'vintage')
        self.assertTrue(os.path.exists(out))
        os.remove(out)

    def test_convert_with_watermark(self):
        out = 'test_out_watermark.pdf'
        converter.convert(self.sample_md, out, 'vintage', watermark='CONFIDENTIAL')
        self.assertTrue(os.path.exists(out))
        os.remove(out)

    def test_convert_with_notes_and_doodles(self):
        out = 'test_out_notes.pdf'
        converter.convert(self.sample_md, out, 'vintage', notes='Note here', doodles=['star'])
        self.assertTrue(os.path.exists(out))
        os.remove(out)

    def test_export_to_epub(self):
        out = 'test_out.epub'
        converter.export_to_format(self.sample_md, out, 'epub')
        self.assertTrue(os.path.exists(out))
        os.remove(out)

    def test_export_to_html(self):
        out = 'test_out.html'
        converter.export_to_format(self.sample_md, out, 'html')
        self.assertTrue(os.path.exists(out))
        os.remove(out)

if __name__ == '__main__':
    unittest.main() 