from bs4 import BeautifulSoup as bs
from urllib2 import urlretrieve, urlopen
import sys
import time
import os
import csv
from re import compile

"""
This is a small tool that automates some of the more tedious tasks of
QAing our migrated web pages.
"""

class qa_tester():

	basedir = os.getcwd()
	URLS = open("urlfile.txt").readlines()

	def __init__(self):
		pass
	
	def check_images(self):
		pass

	def check_urls(self):
		pass

def main():

	tester = qa_tester()

	for url in URLS:
		check_images()
		check_urls()

if __name__ == "__main__":
	main()
