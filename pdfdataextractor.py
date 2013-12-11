"""
Script to extract metadata from PDFs.
"""
from pyPdf import PdfFileReader

BASEDIR = ''
PDFFiles = []

for file in PDFFiles:
	"""
	Processes the files in the PDFFiles list.  If the document 
	is missing data, it will pass and continue so you can 
	inspect the exceptions by hand.
	"""
	try:
		pdf_toread = PdfFileReader(open(BASEDIR + file, 'rb'))
		pdf_info = pdf_toread.getDocumentInfo()
		print file + "--" + pdf_info['/Title'] + " - " + pdf_info['/Subject']
	except:
		print 'null'
		pass
