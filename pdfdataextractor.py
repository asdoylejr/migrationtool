"""
Script to extract metadata from PDFs.
"""
from PyPDF2 import PdfFileReader
#from pdfminer.pdfparser import PDFParser, PDFDocument
import csv
import os
import sys

class pdf_extractor():

    def __init__(self):
        self.basedir = os.getcwd()
        self.pdffiles = []

    def extractor(self):   
        with open('pdfmetadata.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for f in pdf_extractor.pdffiles:
                try:
                    pdf_to_read = PdfFileReader(open(f, 'r'))
                    pdf_info = pdf_to_read.getDocumentInfo()
                    title = pdf_info['/Title']
                    subject = pdf_info['/Subject']
                    writer.writerow([f, title, subject])
                    print 'Metadata for %s written successfully.' % (f)
                except:
                    """
                    Working on alternate reader in case of failure. 

                    pdf_to_read = PDFParser(open(f, 'rb'))
                    doc = PDFDocument
                    """
                else:
                    print 'ERROR reading file %s.' % (f)
                    #print sys.exc_info()
                    writer.writerow([f, 'ERROR', 'ERROR'])
                    pass

def main():

    c = pdf_extractor()

    for x in os.listdir(basedir):
        if x[-3:].lower() == 'pdf':
            pdffiles.append(x)

    c.extractor()

if __name__ == "__main__":
    main()