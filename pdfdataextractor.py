"""
Script to extract metadata from PDFs.
"""
from pyPdf import PdfFileReader

BASEDIR = ''
PDFFiles = []
def extractor():
	output = open('windoutput.txt', 'r+')
	for file in PDFFiles:
		"""
		Processes the files in the PDFFiles list.  If the document 
		is missing data, it will pass and continue so you can 
		inspect the exceptions by hand.
		"""
		try:
			pdf_toread = PdfFileReader(open(BASEDIR + file, 'r'))
			pdf_info = pdf_toread.getDocumentInfo()
			
			#print str(pdf_info)   #print full metadata if you want
			
			x = file + "~" + pdf_info['/Title'] + " ~ " + pdf_info['/Subject']
			print x
			output.write(x + '\n')
		except:
			x = file + '~' + ' ERROR: Data missing or corrupt'
			print x
			output.write(x + '\n')
			pass
	output.close()

if __name__ == "__main__":
	extractor()
