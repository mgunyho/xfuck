"""
Generate xfuck-pdf from brainfuck source code
"""

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY


pdfmetrics.registerFont(TTFont('>', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('<', 'Ayuthaya.ttf'))
pdfmetrics.registerFont(TTFont('+', 'Sathu.ttf'))
pdfmetrics.registerFont(TTFont('-', 'Chalkduster.ttf'))
pdfmetrics.registerFont(TTFont('.', 'Courier New.ttf'))
pdfmetrics.registerFont(TTFont(',', 'Herculanum.ttf'))
pdfmetrics.registerFont(TTFont('[', 'Impact.ttf'))
pdfmetrics.registerFont(TTFont(']', 'Krungthep.ttf'))

bf_symbols = "><+-.,[]"

hw = "+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-."

PDF_NAME = "hello.pdf"

doc = SimpleDocTemplate(PDF_NAME,pagesize=A4,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

LETTER = 'x' # The letter we want to show in PDF

Story = []

# Add each bf-symbol with corre ct font for key
key = "".join(['<font name="' + s + '" size="12">' + LETTER + '</font>' for s in bf_symbols])

Story.append(Paragraph(key, styles["Normal"]))

# Add spacer
Story.append(Spacer(1, 12))


#for i, x in enumerate(hw):
#    c.drawString(100,750-i*10,x)
#c.save()

code = "".join(['<font name="' + s + '" size="12">' + LETTER + '</font>' for s in hw])

Story.append(Paragraph(code, styles["Normal"]))

doc.build(Story)
