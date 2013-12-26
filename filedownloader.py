from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve, urlopen
from re import compile
import os
import sys

URLs = ['http://www1.eere.energy.gov/wind']

BASEURL = ['http://www1.eere.energy.gov/', 'http://www1.eere.energy.gov', 'http://www1.eere.energy.gov/wind/']

FILETYPE = ['\.pdf$','\.ppt$', '\.pptx$', '\.doc$', '\.docx$', '\.xls$', '\.xlsx$', '\.wmv$']

def main():
	for link in soup.findAll(href = compile(types)):
		file = link.get('href')
		filename = file.split('/')[-1]
		
		try:
			urlretrieve(file, filename)
			print file
		except:
			for base in BASEURL:
				try:
					urlretrieve(base + file, filename)
					print base + file
					break
				except:
					print 'Error downloading ' + file
					pass
		
if __name__ == "__main__":

	for url in URLs:
		html_data = urlopen(url)
		soup = BeautifulSoup(html_data)
                
		for types in FILETYPE:
			main()
