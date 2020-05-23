"""
Convert a xf (PDF) file to a brainfuck string
"""

from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTContainer, LTText, LTTextBox, LTImage

from .brainfuck import charset

class BfPDFInterpreter(PDFPageInterpreter):
    def do_TJ(self, seq):
        # instead of rendering a string, check
        f = self.textstate.font.basefont
        n_bf = len(self.device.fontmap)
        if f not in self.device.fontmap and n_bf < 8:
            self.device.fontmap[f] = charset[n_bf]
        return super().do_TJ(seq)

class BfConverter(TextConverter):
    def __init__(self, rsrcmgr, outfp,
                 codec='utf-8', pageno=1, laparams=None,
                 showpageno=False, imagewriter=None):
        super().__init__(rsrcmgr, outfp, codec=codec, pageno=pageno, laparams=laparams,
                 showpageno=showpageno, imagewriter=imagewriter)

        # mapping from font basefont name to brainfuck character
        # populated by the interpreter (maximum spaghetti)
        self._fontmap = {}
        return

    @property
    def fontmap(self):
        return self._fontmap

    def receive_layout(self, ltpage):
        # copy pasted from superclass to override render
        def render(item):
            if isinstance(item, LTContainer):
                for child in item:
                    render(child)
            elif isinstance(item, LTText):
                #self.write_text(item.get_text())
                #TODO: newlines ????
                if hasattr(item, "fontname"):
                    #self.write_brainfuck(item.get_text(), item.fontname)
                    fn = item.fontname
                    if fn in self.fontmap:
                        self.write_text(self.fontmap[fn])
            if isinstance(item, LTTextBox):
                #self.write_text('\n')
                pass
            elif isinstance(item, LTImage):
                if self.imagewriter is not None:
                    self.imagewriter.export_image(item)
        if self.showpageno:
            #self.write_text('Page %s\n' % ltpage.pageid)
            pass
        render(ltpage)
        #self.write_text('\f')
        return


def xf2bf(pdf_filename: str, strip_charset=True) :
    """
    Convert the given xf/pdf file to a brainfuck string.

    Based on pdfminer.high_level.extract_text
    """
    mgr = PDFResourceManager()
    out_str = StringIO()
    dev = BfConverter(mgr, out_str, codec="utf-8")
    interp = BfPDFInterpreter(mgr, dev)

    with open(pdf_filename, "rb") as f:
        for p in PDFPage.get_pages(
                f,
                #maxpages=999, #TODO: is this necessary?
            ):
                interp.process_page(p)

    ret = out_str.getvalue()
    if strip_charset:
        ret = ret[8:]
    return ret
