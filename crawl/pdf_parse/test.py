from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator 
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


# Open a PDF file.
#fp = open('zh_CN.pdf', 'rb')
fp = open('阿里巴巴Java开发手册终极版v1.3.0.pdf', 'rb')
#fp = open('毛泽东选集1.pdf', 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
doc = PDFDocument()

# Connect the parser and document objects.
parser.set_document(doc)
doc.set_parser(parser)

# Supply the password for initialization.
# (If no password is set, give an empty string.)
password = ''
doc.initialize(password)

# Check if the document allows text extraction. If not, abort.
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            print(element.get_text())
    

