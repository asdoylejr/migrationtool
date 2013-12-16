from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve, urlopen
#from urllib2 import urlopen
from re import compile
import os
import sys

URLs = ['http://www1.eere.energy.gov/water/2011_peer_review.html']
BASEURL = ['http://www1.eere.energy.gov', 'http://www1.eere.energy.gov/water/']
FILETYPE = ['\.pdf$','\.ppt$', '\.pptx$']

def pdf():
        for link in soup.findAll(href = compile(types)):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        #urlretrieve(BASEURL[0] + file, filename)
                        print BASEURL[0] + file
                elif file [0:2] == "pdf":
                       # urlretrieve(BASEURL[1] + file, filename)
                        print BASEURL[1] + file
                else:
                       # urlretrieve(file, filename)
                        print file

if __name__ == "__main__":
        for url in URLs:
                html_data = urlopen(url)
                soup = BeautifulSoup(html_data)
                
                for types in FILETYPE:
                        pdf()
"""                       
def ppt():
        for link in soup.findAll(href = compile(FILETYPE[0])):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        urlretrieve(BASEURL[0] + file, filename)
                        print BASEURL[0] + file
                elif file [0:2] == "pdf":
                        urlretrieve(BASEURL[1] + file, filename)
                        print BASEURL[1] + file
                else:
                        urlretrieve(file, filename)
                        print file

def pptx():
        for link in soup.findAll(href = compile('\.pptx$')):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        urlretrieve(BASEURL[0] + file, filename)
                        print BASEURL[0] + file
                elif file [0:2] == "pdf":
                        urlretrieve(BASEURL[1] + file, filename)
                        print BASEURL[1] + file
                else:
                        urlretrieve(file, filename)
                        print file

def pdf():
        for link in soup.findAll(href = compile(types)):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        urlretrieve(BASEURL[0] + file, filename)
                        print BASEURL[0] + file
                elif file [0:2] == "pdf":
                        urlretrieve(BASEURL[1] + file, filename)
                        print BASEURL[1] + file
                else:
                        urlretrieve(file, filename)
                        print file

def doc():
        for link in soup.findAll(href = compile('\.doc$')):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        try:
                                #urlretrieve(BASEURL[0] + file, filename)
                                print BASEURL[0] + file
                        except:
                                #urlretrieve(BASEURL[1] + file, filename)
                                print BASEURL[1] + file
                else:
                        #urlretrieve(file, filename)
                        print file

def docx():
        for link in soup.findAll(href = compile('\.docx$')):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        try:
                                #urlretrieve(BASEURL[0] + file, filename)
                                print BASEURL[0] + file
                        except:
                                #urlretrieve(BASEURL[1] + file, filename)
                                print BASEURL[1] + file
                else:
                        #urlretrieve(file, filename)
                        print file

def excel():
        for link in soup.findAll(href = compile('\.xls$')):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        try:
                                #urlretrieve(BASEURL[0] + file, filename)
                                print BASEURL[0] + file
                        except:
                                #urlretrieve(BASEURL[1] + file, filename)
                                print BASEURL[1] + file
                else:
                        #urlretrieve(file, filename)
                        print file

def excelx():
        for link in soup.findAll(href = compile('\.xlsx$')):
                file = link.get('href')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        try:
                                #urlretrieve(BASEURL[0] + file, filename)
                                print BASEURL[0] + file
                        except:
                                #urlretrieve(BASEURL[1] + file, filename)
                                print BASEURL[1] + file
                else:
                        #urlretrieve(file, filename)
                        print file

def jpg():
        for link in soup.findAll(src = compile('\.jpg$')):
                file = link.get('src')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        try:
                                #urlretrieve(BASEURL[0] + file, filename)
                                print url + ":  " + BASEURL[0] + file
                        except:
                                #urlretrieve(BASEURL[1] + file, filename)
                                print url + ":  " + BASEURL[1] + file
                else:
                        #urlretrieve(file, filename)
                        print url + ":  " + file

def png():
        for link in soup.findAll(src = compile('\.png$')):
                file = link.get('src')
                filename = file.split('/')[-1]
                if file[0] == "/":
                        try:
                                #urlretrieve(BASEURL[0] + file, filename)
                                print url + ":  " + BASEURL[0] + file
                        except:
                                #urlretrieve(BASEURL[1] + file, filename)
                                print url + ":  " + BASEURL[1] + file
                else:
                        #urlretrieve(file, filename)
                        print url + ":  " + file

if __name__ == "__main__":
        for url in URLs:
                html_data = urlopen(url)
                soup = BeautifulSoup(html_data)
                
                for types in FILETYPE:
                        pdf()
                #ppt()
                #pptx()
                #jpg()
                #png()
               # excel()
               # excelx()
               # doc()
               # docx()
"""