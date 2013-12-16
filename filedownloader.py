from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve, urlopen
#from urllib2 import urlopen
from re import compile
import os
import sys

'''
Insert a list of URLs here to crawl through.
'''
URLs = []
'''
Insert base urls here in case entire links are not referenced.
'''
BASEURL = []
FILETYPE = ['\.pdf$','\.ppt$', '\.pptx$', '\.doc$', '\.docx$', '\.xls$', '\.xlsx$',
'\.wmv$']

def main():
        for link in soup.findAll(href = compile(types)):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        urlretrieve(BASEURL[0] + file, filename)
                        print BASEURL[0] + file
                """
                Need to work on further exceptions.......

                elif file [0:2] == "pdf":
                       urlretrieve(BASEURL[1] + file, filename)
                        print BASEURL[1] + file
                """
                else:
                       urlretrieve(file, filename)
                        print file

if __name__ == "__main__":

        for url in URLs:
                html_data = urlopen(url)
                soup = BeautifulSoup(html_data)
                
                for types in FILETYPE:
                        main()
