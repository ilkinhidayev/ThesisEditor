from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def convert_to_guidelines(docx_path):
    doc = Document(docx_path)

    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)

    # Modify paragraphs and headings
    for paragraph in doc.paragraphs:
        if paragraph.style.name.startswith('Heading 1'):
            for run in paragraph.runs:
                run.font.bold = True
                run.font.size = Pt(14)
            paragraph.text = paragraph.text.upper()
        elif paragraph.style.name.startswith('Heading'):
            for run in paragraph.runs:
                run.font.bold = True

        paragraph.paragraph_format.line_spacing = 1.5
        paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        # More modifications as per the other requirements...

    # Set page margins
    sections = doc.sections
    for section in sections:
        section.left_margin = Cm(3.5)
        section.right_margin = Cm(2.5)
        section.top_margin = Cm(3)
        section.bottom_margin = Cm(3)
        # Page number can be added using a footer. It's a bit more complex.
    
    # Save the modified document
    converted_path = docx_path.replace('.docx', '_converted.docx')
    doc.save(converted_path)

    return converted_path
