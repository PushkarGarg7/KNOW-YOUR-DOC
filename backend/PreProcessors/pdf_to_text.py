import fitz  # PyMuPDF

class PDFToText:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        # Open the document
        doc = fitz.open(self.file_path)
        text = []
        for page in doc:
            text.append(page.get_text())
        doc.close()
        return "\n".join(text)
