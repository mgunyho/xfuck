from collections import OrderedDict
from pdfrw import PdfReader

def get_key(pdf: PdfReader):
    keys = list()
    for s in pdf.pages[0].Contents.stream.split(" "):
        if len(keys) == 8:
            break
        if s.startswith("/TT") and s not in keys:
            keys.append(s)

    if len(keys) < 8:
        raise SyntaxError("Less than 8 fonts found")

    return OrderedDict([(k, pdf.pages[0].Resources.Font[k]) for k in keys])
