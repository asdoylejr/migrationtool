"""
Script to extract metadata from PDFs.
"""
from pyPdf import PdfFileReader

BASEDIR = 'Water_Files/'
PDFFiles = ['11_wwf_principle_power_weinstein.pdf']

for file in PDFFiles:
	"""
	Processes the files in the PDFFiles list.  If the document 
	is missing data, it will pass and continue so you can 
	inspect the exceptions by hand.
	"""
	try:
		pdf_toread = PdfFileReader(open(BASEDIR + file, 'rb'))
		pdf_info = pdf_toread.getDocumentInfo()
		#print str(pdf_info)   #print full metadata if you want
		print file + "--" + pdf_info['/Title'] + " - " + pdf_info['/Subject']
	except:
		print 'null'
		pass
