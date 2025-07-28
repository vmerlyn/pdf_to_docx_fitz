from pathlib import Path
from docx import Document
import fitz  # PyMuPDF


class PDFConverter:
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

    def convert_to_docx(self, output_path: Path) -> Path:
        doc = Document()
        with fitz.open(str(self.pdf_path)) as pdf:
            for page in pdf:
                text = page.get_text()
                if text:
                    doc.add_paragraph(text)
        doc.save(output_path)
        return output_path
