#!/usr/bin/env python3
"""
Generate xfuck-pdf from brainfuck source code
"""

#from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from pathlib import Path

# Initialize all brainfuck font associations
pdfmetrics.registerFont(TTFont('>', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('<', 'Ayuthaya.ttf'))
pdfmetrics.registerFont(TTFont('+', 'Sathu.ttf'))
pdfmetrics.registerFont(TTFont('-', 'Chalkduster.ttf'))
pdfmetrics.registerFont(TTFont('.', 'Courier New.ttf'))
pdfmetrics.registerFont(TTFont(',', 'Herculanum.ttf'))
pdfmetrics.registerFont(TTFont('[', 'Impact.ttf'))
pdfmetrics.registerFont(TTFont(']', 'Krungthep.ttf'))

BF_CHARS = "><+-.,[]" # Characters of brainfuck

def single_char_encoder(bf_char, display_char):
    """
    Returns string for paragraph builder containing font information (from bf_char) and displayed character (display_char)
    """
    return '<font name="' + bf_char + '" size="12">' + display_char + '</font>'


def bf_string_2_pdf(brainfuck_string, file_name):
    """
    Creates PDF file (file_name) that includes brainfuck code (brainfuck_string) encoded using fonts defined above.
    """
    doc = SimpleDocTemplate(file_name, pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(fontName='>', name='Justify', alignment=TA_JUSTIFY))

    brainfuck_string = brainfuck_string.replace(" ", "").replace("\n", "")

    display_char = 'x' # The letter we want to show in PDF

    Story = []

    # Add each bf-symbol with corre ct font for key
    key = "".join([single_char_encoder(bf, display_char) for bf in BF_CHARS])

    Story.append(Paragraph(key, styles["Normal"]))

    # Add spacer
    Story.append(Spacer(1, 12))

    code = "".join([single_char_encoder(bf, display_char) for bf in brainfuck_string])

    Story.append(Paragraph(code, styles["Normal"]))

    doc.build(Story)


def bf_file_2_pdf(path_to_bf):
    """
    Gets path to brainfuck file (path/to/brain.bf) as parameter,
    and produces pdf into same location where script is run
    """
    with open('path_to_bf', 'r') as file:
        bf = file.read().replace('\n', '')

    name = Path(path_to_bf).stem

    bf_string_2_pdf(bf, name+".pdf")


if __name__ == '__main__':
    hw = "+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-."
    PDF_NAME = "../examples/hello-2.pdf"

    bf_string_2_pdf(hw, PDF_NAME)
