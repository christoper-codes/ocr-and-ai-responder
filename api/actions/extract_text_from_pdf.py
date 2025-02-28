import fitz  # PyMuPDF

class ExtractTextFromPDF:
    @staticmethod
    def execute(file):
        text = ''
        pdf_document = fitz.open(stream=file.read(), filetype='pdf')
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        return text