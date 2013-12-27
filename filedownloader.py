from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve, urlopen
from re import compile
import os
import sys
import urlparse

URLs = ['http://www1.eere.energy.gov/wind']

BASEURL = ['http://www1.eere.energy.gov/', 'http://www1.eere.energy.gov', 'http://www1.eere.energy.gov/wind/']

FILETYPE = ['\.pdf$','\.ppt$', '\.pptx$', '\.doc$', '\.docx$', '\.xls$', '\.xlsx$', '\.wmv$']

def main(soup, domain, path, types):
	for link in soup.findAll(href = compile(types)):
		file = link.get('href')
		filename = file.split('/')[-1]
		
		if '://' not in file and not file.startswith('//'):
			if not file.startswith('/'):
				file = urlparse.urljoin(path, file)
			file = urlparse.urljoin(domain, file)
		
		try:
			urlretrieve(file, filename)
			print file
		except:
			print 'Error retrieving %s using URL %s' % (link.get('href'), file)
		
		
if __name__ == "__main__":

	for url in URLs:
		html_data = urlopen(url)
		soup = BeautifulSoup(html_data)
		
		urlinfo = urlparse.urlparse(url)
		domain = urlparse.urlunparse((urlinfo.scheme, urlinfo.netloc, '', '', '', ''))
		path = urlinfo.path.rsplit('/', 1)[0]
                
		for types in FILETYPE:
			main(soup, domain, path, types)
