from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve
from urllib2 import urlopen
from re import compile
import os
import sys

URLs = ['http://www1.eere.energy.gov/water/']
BASEURL = ['http://www1.eere.energy.gov', 
'http://apps1.eere.energy.gov']


def pdf():
	for link in soup.findAll(href = compile('\.pdf$')):
		file = link.get('href')
		filename = file.split('/')[-1]
		try:	
			if file[0] == "/":
				try:
					urlretrieve(BASEURL[0] + file, filename)
					print BASEURL + file
				except:
					urlretrieve(BASEURL[1] + file, filename)
					print BASEURL + file
			else:
				urlretrieve(file, filename)
				print file
		except:
			print "Error downloading" + file
			pass
"""
def docs():
	for link in soup.findAll(href = compile('\.pdf$')):
		file = link.get('href')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve(BASEURL + file, filename)
			print BASEURL + file
		else:
			urlretrieve(file, filename)
			print file

def excel():
	for link in soup.findAll(href = compile('\.xls$')):
		file = link.get('href')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve(BASEURL + file, filename)
			print BASEURL + file
		else:
			urlretrieve(file, filename)
			print file

def jpg():
	for link in soup.findAll(src = compile('\.jpg$')):
		file = link.get('src')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve(BASEURL + file, filename)
			print BASEURL + file
		else:
			urlretrieve(file, filename)
			print file

def png():
	for link in soup.findAll(src = compile('\.png$')):
		file = link.get('src')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve(BASEURL + file, filename)
			print BASEURL + file
		else:
			urlretrieve(file, filename)
			print file
"""

if __name__ == "__main__":
	for url in URLs:
		soup = BeautifulSoup(urlopen(url))
		pdfs()
		#jpg()
		#png()
		#excel()
		#docs()
