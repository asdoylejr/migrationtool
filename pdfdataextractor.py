"""
Script to extract metadata from PDFs.
"""
import glob
from pyPdf2 import PdfFileReader
import csv
import os
import sys

def extractor():	
	basedir = os.getcwd()
	pdffiles = []
	for x in os.listdir(basedir):
		if x[-3:] == 'pdf':
			pdffiles.append(x)
	
	with open('pdfmetadata.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		for f in pdffiles:
			try:
				pdf_to_read = PdfFileReader(open(f, 'r'))
				pdf_info = pdf_to_read.getDocumentInfo()
				title = pdf_info['/Title']
				subject = pdf_info['/Subject']
				writer.writerow([f, title, subject])
				print 'Metadata for %s written successfully.' % (f)
			except:
				print 'ERROR reading file %s.' % (f)
				#print sys.exc_info()
				writer.writerow([f, 'ERROR', 'ERROR'])
				pass

if __name__ == "__main__":
	extractor()