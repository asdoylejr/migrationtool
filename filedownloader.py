from bs4 import BeautifulSoup as bs
import csv
from urllib import urlretrieve, urlopen
from re import compile
import sys
import time
import urlparse
import os

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
        with open('data.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for url in downloadtools.URLS:
                try:
                    html_data = urlopen(url)
                except:
                    print 'Error opening URL: ' + url
                    pass
                
                #Creates a BS object out of the open URL.
                soup = bs(html_data)
                #Parsing the URL for later use
                urlinfo = urlparse.urlparse(url)
                domain = urlparse.urlunparse((urlinfo.scheme, urlinfo.netloc, '', '', '', ''))
                path = urlinfo.path.rsplit('/', 1)[0]

                #Creates nested directories to save the files based on the
                #base URL path to avoid removal of duplicates.
                webfile = urlinfo.path.split('/')[-1]
                folderdir = urlinfo.path.replace(webfile, "").lstrip('/')
                if not os.path.exists(folderdir):
                    os.makedirs(folderdir)
                os.chdir(folderdir)
                
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
                            urlretrieve(file, filename, Percentage)
                            os.chdir(downloadtools.basedir)
                            writer.writerow(["SUCCESS", url, file, filename])
                            os.chdir(folderdir)
                            print "     SUCCESS"
                        except:
                            os.chdir(downloadtools.basedir)
                            writer.writerow(["ERROR", url, file, filename])
                            os.chdir(folderdir)
                            print "     ERROR"
                os.chdir(downloadtools.basedir)

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

def main():
    bot = downloadtools()
    bot.downloader()

if __name__ == '__main__':
    main()