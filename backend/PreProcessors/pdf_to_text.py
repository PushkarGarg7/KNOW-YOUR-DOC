# import fitz  # PyMuPDF

# class PDFToText:
#     def __init__(self, file_path):
#         self.file_path = file_path

#     def extract_text(self):
#         # Open the document
#         doc = fitz.open(self.file_path)
#         text = []
#         for page in doc:
#             text.append(page.get_text())
#         doc.close()
#         return "\n".join(text)

from PyPDF2 import PdfReader

class PDFToText:
    def __init__(self, file_content):
        self.file_content = file_content

    def extract_text(self):
        pdf_reader = PdfReader(self.file_content)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text

