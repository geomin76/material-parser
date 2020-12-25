# from pdfminer.high_level import extract_text
import textract

def parse_pdf(filename):
    # text = extract_text('sample.PDF')
    # print(repr(text))
    # ls = text.split()
    # ls = text.split('\n')
    # print(ls)
    print("ok")

def parse_doc(filename):
    text = textract.process('sample.DOCX')
    ls = text.split(b'\n\n')
    print(ls)

if __name__ == "__main__":
    print("hello world")
    # parse_pdf('')
    parse_doc('')