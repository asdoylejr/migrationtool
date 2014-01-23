from urllib import urlretrieve
import time
import sys

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
	
	URLS = open("urlfile.txt").readlines()
	
	for url in URLS:
		filename = url.rstrip().split('/')[-1]
		try:
			urlretrieve(url, filename, Percentage)
			print "Successful download: %s" % filename
		except:
			print "Error downloading %s" % filename
			
if __name__ == "__main__":
	Downloader()
