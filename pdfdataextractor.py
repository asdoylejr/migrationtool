"""
Script to extract metadata from PDFs.
"""
from PyPDF2 import PdfFileReader
#from pdfminer.pdfparser import PDFParser, PDFDocument
import csv
import os
import sys

class pdf_extractor():   
    basedir = os.getcwd()
    pdffiles = []
    for x in os.listdir(basedir):
        if x[-3:] == 'pdf':
            pdffiles.append(x)

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

if __name__ == "__main__":
    c = pdf_extractor()
    c.extractor()