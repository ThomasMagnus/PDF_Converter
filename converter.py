from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import docx


class PDFConverter:

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.rsrcmgr = PDFResourceManager()
        self.retstr = StringIO()
        self.codec = 'utf-8'
        self.laparams = LAParams()
        self.device = TextConverter(self.rsrcmgr, self.retstr, self.codec, laparams=self.laparams)
        self.fp = open(self.path, 'rb')
        self.interpreter = PDFPageInterpreter(rsrcmgr=self.rsrcmgr, device=self.device)
        self.password = ''
        self.maxpages = 0
        self.caching = True
        self.pagenos = set()

    def converter_to_text(self):
        for page in PDFPage.get_pages(self.fp, self.pagenos, maxpages=self.maxpages, password=self.password,
                                      caching=self.caching,
                                      check_extractable=True):
            self.interpreter.process_page(page)

        text = self.retstr.getvalue()

        self.fp.close()
        self.device.close()
        self.retstr.close()
        return text.replace('', '')

    def convert_to_word(self):
        text = self.converter_to_text()
        my_docx = docx.Document()
        my_docx.add_paragraph(text)
        my_docx.save(f'./home/{self.name}.docx')

