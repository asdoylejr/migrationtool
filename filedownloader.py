from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve, urlopen
from re import compile
import os
import sys
import urlparse

#A list of file types for the script to iterate through for every URL.
FILETYPE = ['\.pdf$','\.ppt$', '\.pptx$', '\.doc$', '\.docx$', '\.xls$', '\.xlsx$', '\.wmv$']

#The main function.  Identifies and downloads all of the links with file
#extensions inside of each BeautifulSoup object.
def main(soup, domain, path, types):
	for link in soup.findAll(href = compile(types)):
		file = link.get('href')
		filename = file.split('/')[-1]
		
		if '://' not in file and not file.startswith('//'):
			if not file.startswith('/'):
				file = urlparse.urljoin(path, file)
			file = urlparse.urljoin(domain, file)
		
		#Attempts to download each file and returns an error with the file so
		#that it can be dealt with manually.
		try:
			#urlretrieve(file, filename)
			print url, ': ', file
		except:
			print 'Error retrieving %s using URL %s' % (link.get('href'), file)
		
		
if __name__ == "__main__":

	with open('urlfile.txt', 'rU') as f:
		for url in f:
			html_data = urlopen(url)
			soup = BeautifulSoup(html_data)
		
			urlinfo = urlparse.urlparse(url)
			domain = urlparse.urlunparse((urlinfo.scheme, urlinfo.netloc, '', '', '', ''))
			path = urlinfo.path.rsplit('/', 1)[0]
		     
		    #With each URL the script searches for all listed file types.      
			for types in FILETYPE:
				main(soup, domain, path, types)
