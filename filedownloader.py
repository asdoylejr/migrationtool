from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve, urlopen
from re import compile
import sys
import time
import urlparse

"""
List of file types for the script to search for.
"""
FILETYPE = ['\.pdf$','\.ppt$', '\.pptx$', '\.doc$', '\.docx$', '\.xls$', '\.xlsx$', '\.wmv$', '\.mp3$', '\.f4v$', '\.mp4$']

"""
Function that prints out progress data on the current download.
"""
def Percentage(count, block_size, total_size):
	global start_time
	
	if count == 0:
		start_time = time.time()
		return
	duration = time.time() - start_time
	progress_size = int(count * block_size)
	speed = int(progress_size / (1024 * duration))
	percent = min(int(count * block_size * 100 / total_size), 100)
	sys.stdout.write("\r...%d%%, %d MB, %d KB/s" % (percent, progress_size / (1024 * 1024), speed))
	sys.stdout.flush()

"""
Function that iterates through a list of URLs in a text file, searching
for asset files to download.
"""
def Downloader():

	#Open up the text file with the list of URLs
	with open('urlfile.txt', 'rU') as f:	
		#Attempts to open the URL or returns an error and passes.
		for url in f:
			try:
				html_data = urlopen(url)
			except:
				print 'Error opening URL: ' + url
				pass
			
			#Creates a BS object out of the open URL.
			soup = BeautifulSoup(html_data)
			#Parsing the URL for later use
			urlinfo = urlparse.urlparse(url)
			domain = urlparse.urlunparse((urlinfo.scheme, urlinfo.netloc, '', '', '', ''))
			path = urlinfo.path.rsplit('/', 1)[0]
			
			#Loop iterates through list of file types for open URL.
			for types in FILETYPE:
				for link in soup.findAll(href = compile(types)):
					file = link.get('href')
					filename = file.split('/')[-1]
					
					#Creates a full URL if needed.
					if '://' not in file and not file.startswith('//'):
						if not file.startswith('/'):
							file = urlparse.urljoin(path, file)
						file = urlparse.urljoin(domain, file)
					
					#Downloads the file or returns error for manual inspection
					try:
						print url, ': ', file
						urlretrieve(file, filename, Percentage)		
					except:
						print 'Error retrieving %s ursing URL %s' % (link.get('href'), file)

if __name__ == '__main__':
	Downloader()
		
