import pdfplumber
import mammoth
import markdown

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_text_from_docx(docx_path):
    with open(docx_path, 'rb') as docx_file:
        result = mammoth.extract_raw_text(docx_file)
        extracted_text = result.value

        return extracted_text

def parse_markdown_to_text(markdown_text):
    html = markdown.markdown(markdown_text)
    return html
