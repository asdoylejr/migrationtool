from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve, urlopen
from re import compile
import sys
import time
import urlparse

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
	
	#Open up the text file full of URLs as a list.
	URLS = open("urlfile.txt").readlines()
	
	#Attempts to open the URL or returns an error and passes.
	for url in URLS:
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
		
		FILETYPE = ['\.pdf$', '\.ppt$', '\.pptx$', '\.doc$', '\.docx$', '\.xls$', '\.xlsx$', '\.wmv$', '\.mp4$', '\.mp3$']

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
					print 'Error retrieving %s ursing URL %s' % (filename, file)

			#for link in 

"""
Iterates through a list of specific download URLs and downloads them.
"""
def SimpleDownloader():
	
	URLS = open("urlfile.txt").readlines()
	
	for url in URLS:
		filename = url.rstrip().split('/')[-1]
		try:
			urlretrieve(url, filename, Percentage)
			print "Successful download: %s" % filename
		except:
			print "Error downloading %s" % filename

if __name__ == '__main__':
	options = "ATTENTION: Ensure file 'urlfile.txt' is properly populated before continuing.\n\
	\n\
Options:\n\
	\n\
1. Parse a list of URLs to find downloadable content.\n\
2. Download files from a pre-existing list of URLs.\n\
3. Please explain configuring the URLs.\n"
	print options
	user_input = int(raw_input("Input number option you'd like to execute: "))
	if user_input == 1:
		print "Searching URL list for possible downloads."
		Downloader()
	elif user_input == 2:
		print "Downloading files from list."
		SimpleDownloader()
	elif user_input == 3:
		print "***************************************************************************\n\
INSTRUCTIONS: in the same directory you are working with this file,\n\
create a file titled 'urlfile.txt', if you do not have one already.\n\
Populate the file with your URLs, either page URLs in which to search\n\
for downloads, or a list of direct download links to automaticallydownload.\n\
***************************************************************************"
		print options