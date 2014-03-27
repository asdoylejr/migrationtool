from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve, urlopen
from re import compile
import sqlite3 as lite
import sys
import time
from urllib.parse import urlparse, urlunparse, urljoin
import os
import csv

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
for files to download, and downloads them, placing in embedded folders.
"""

class downloadtools():
   
    basedir = os.getcwd()
    URLS = open("urlfile.txt").readlines()

    def __init__(self):
        pass

    def downloader(self):
        with open('data.csv', 'w') as datafile:
            writer = csv.writer(datafile)
            for url in downloadtools.URLS:
                try:
                    html_data = urlopen(url)
                except Exception as e:
                    print('Error opening URL: ' + url, e)
                    writer.writerow([url])
                    pass
                
                #Creates a BS object out of the open URL.
                soup = bs(html_data)
                #Parsing the URL for later use
                urlinfo = urlparse(url)
                domain = urlunparse((urlinfo.scheme, urlinfo.netloc, '', '', '', ''))
                path = urlinfo.path.rsplit('/', 1)[0]

                FILETYPE = ['\.pdf$', '\.ppt$', '\.pptx$', '\.doc$', '\.docx$', '\.xls$', '\.xlsx$', '\.wmv$', '\.mp4$', '\.mp3$']

                #Loop iterates through list of file types for open URL.
                for types in FILETYPE:
                    for link in soup.findAll(href = compile(types)):
                        urlfile = link.get('href')
                        filename = urlfile.split('/')[-1]
                        while os.path.exists(filename):
                            try:
                                fileprefix = filename.split('_')[0]
                                filetype = filename.split('.')[-1]
                                num = int(filename.split('.')[0].split('_')[1])
                                filename = fileprefix + '_' + str(num + 1) + '.' + filetype
                            except Exception as e:
                                filetype = filename.split('.')[1]
                                fileprefix = filename.split('.')[0] + '_' + str(1)
                                filename = fileprefix + '.' + filetype
                                print e
                        
                        #Creates a full URL if needed.
                        if '://' not in urlfile and not urlfile.startswith('//'):
                            if not urlfile.startswith('/'):
                                urlfile = urljoin(path, urlfile)
                            urlfile = urljoin(domain, urlfile)
                        
                        #Downloads the urlfile or returns error for manual inspection
                        try:
                            urlretrieve(urlfile, filename, Percentage)
                            print('success')
                            writer.writerow([url, urlfile, filename])
                        except Exception as e:
                            writer.writerow(['ERROR', url, urlfile, filename])
                            print('error', e)

    """
    Iterates through a list of specific download URLs and downloads them.
    """

    def simple_downloader(self):
        for url in downloadtools.URLS:
            filename = url.rstrip().split('/')[-1]
            try:
                urlretrieve(url, filename, Percentage)
                print "Successful download: %s" % filename
            except:
                print "Error downloading %s" % filename

if __name__ == '__main__':
    bot = downloadtools()
    bot.downloader()