import pdfplumber
import docx
import markdown

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)

def parse_markdown_to_text(markdown_text):
    html = markdown.markdown(markdown_text)
    return html
