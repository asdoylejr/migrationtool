from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve, urlopen
from re import compile
import sys
import time
import urlparse

FILETYPE = ['\.pdf$','\.ppt$', '\.pptx$', '\.doc$', '\.docx$', '\.xls$', '\.xlsx$', '\.wmv$', '\.mp3$', '\.f4v$', '\.mp4$']

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

def Downloader():
	with open('urlfile.txt', 'rU') as f:
		for url in f:
			try:
				html_data = urlopen(url)
			except:
				print 'Error opening URL: ' + url
				pass
	
			soup = BeautifulSoup(html_data)
			urlinfo = urlparse.urlparse(url)
			domain = urlparse.urlunparse((urlinfo.scheme, urlinfo.netloc, '', '', '', ''))
			path = urlinfo.path.rsplit('/', 1)[0]
		
			for types in FILETYPE:
				for link in soup.findAll(href = compile(types)):
					file = link.get('href')
					filename = file.split('/')[-1]
				
					if '://' not in file and not file.startswith('//'):
						if not file.startswith('/'):
							file = urlparse.urljoin(path, file)
						file = urlparse.urljoin(domain, file)
				
					try:
						print url, ': ', file
						urlretrieve(file, filename, Percentage)		
					except:
						print 'Error retrieving %s ursing URL %s' % (link.get('href'), file)

if __name__ == '__main__':
	Downloader()
		
