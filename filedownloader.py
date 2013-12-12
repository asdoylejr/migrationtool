from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve
from urllib2 import urlopen
from re import compile
import os
import sys

URLs = ['http://www1.eere.energy.gov/water/']
BASEURL = ['http://www1.eere.energy.gov', 
'http://apps1.eere.energy.gov']
#FILETYPE = ['.pdf', '.jpg', '.png']
#TAG = ['href', 'src']

def download(arg1, arg2):
	if arg1[0] == "/":
		try:
			urlretrieve(BASEURL[0] + arg1, arg2)
			print BASEURL[0] + arg1
		except:
			urlretrieve(BASEURL[1] + arg1, arg2)
			print BASEURL[1] + arg1
	else:
		urlretrieve(arg1, arg2)
		print arg1

def pdfs():
	for link in soup.findAll(href = compile('\.pdf$')):
		file = link.get('href')
		filename = file.split('/')[-1]
			
		download(file, filename)
	
def docs():
	for link in soup.findAll(href = compile('\.doc$')):
		file = link.get('href')
		filename = file.split('/')[-1]
	
	download(file, filename)

def excel():
	for link in soup.findAll(href = compile('\.xls$')):
		file = link.get('href')
		filename = file.split('/')[-1]
	
	download(file, filename)

def jpg():
	for link in soup.findAll(src = compile('\.jpg$')):
		file = link.get('src')
		filename = file.split('/')[-1]
	
	download(file, filename)

def png():
	for link in soup.findAll(src = compile('\.png$')):
		file = link.get('src')
		filename = file.split('/')[-1]
	
	download(file, filename)


if __name__ == "__main__":
	for url in URLs:
		soup = BeautifulSoup(urlopen(url))
		pdfs()
		jpg()
		png()
		excel()
		docs()
