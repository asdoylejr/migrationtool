from BeautifulSoup import BeautifulSoup
from urllib import urlretrieve
from urllib2 import urlopen
from re import compile
import os
import sys

URLs = ['http://www1.eere.energy.gov/water/',
'http://www1.eere.energy.gov/water/about.html',
'http://www1.eere.energy.gov/water/activities.html',
'http://www1.eere.energy.gov/library/pir_publicationsnew.aspx/page/14',
'http://www1.eere.energy.gov/water/budget.html',
'http://www1.eere.energy.gov/water/program_peer_reviews.html',
'http://www1.eere.energy.gov/water/2011_peer_review.html',
'http://www1.eere.energy.gov/water/contacts.html',
'http://www1.eere.energy.gov/water/research.html',
'http://www1.eere.energy.gov/water/hydropower.html',
'http://www1.eere.energy.gov/water/hydro_technology_development.html',
'http://www1.eere.energy.gov/water/hydro_market_acceleration.html',
'http://www1.eere.energy.gov/water/hydro_assessment_characterization.html',
'http://www1.eere.energy.gov/water/marine_hydrokinetic.html',
'http://www1.eere.energy.gov/water/marine_technology_development.html',
'http://www1.eere.energy.gov/water/marine_market_acceleration.html',
'http://www1.eere.energy.gov/water/marine_assessment_characterization.html',
'http://www1.eere.energy.gov/water/financial_opportunities.html',
'http://www1.eere.energy.gov/water/past_opportunities.html',
'http://www1.eere.energy.gov/water/related_opportunities.html',
'http://www1.eere.energy.gov/water/resources.html',
'http://www1.eere.energy.gov/water/hydropower_resources.html',
'http://www1.eere.energy.gov/water/how_hydropower_works.html',
'http://www1.eere.energy.gov/water/hydro_plant_types.html',
'http://www1.eere.energy.gov/water/hydro_turbine_types.html',
'http://www1.eere.energy.gov/water/hydro_benefits.html',
'http://www1.eere.energy.gov/water/hydro_history.html',
'http://www1.eere.energy.gov/water/hydro_glossary.html',
'http://www1.eere.energy.gov/water/marine_hydro_resources.html',
'http://www1.eere.energy.gov/water/marine_hydro_glossary.html',
'http://www1.eere.energy.gov/water/related_links.html',
'http://www1.eere.energy.gov/water/news.html',
'http://www1.eere.energy.gov/water/subscribe.html',
'http://www1.eere.energy.gov/water/events.html',
'http://www1.eere.energy.gov/water/contacts_landing.html',
'http://www1.eere.energy.gov/water/webmaster.html',
]

def pdfs():
	for link in soup.findAll(href = compile('\.pdf$')):
		file = link.get('href')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve('http://www1.eere.energy.gov' + file, filename)
			print 'http://www1.eere.energy.gov' + file
		else:
			urlretrieve(file, filename)
			print file

def docs():
	for link in soup.findAll(href = compile('\.doc$')):
		file = link.get('href')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve('http://www1.eere.energy.gov' + file, filename)
			print 'http://www1.eere.energy.gov' + file
		else:
			urlretrieve(file, filename)
			print file

def excel():
	for link in soup.findAll(href = compile('\.xls$')):
		file = link.get('href')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve('http://www1.eere.energy.gov' + file, filename)
			print 'http://www1.eere.energy.gov' + file
		else:
			urlretrieve(file, filename)
			print file

def jpg():
	for link in soup.findAll(src = compile('\.jpg$')):
		file = link.get('src')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve('http://www1.eere.energy.gov' + file, filename)
			print 'http://www1.eere.energy.gov' + file
		else:
			urlretrieve(file, filename)
			print file

def png():
	for link in soup.findAll(src = compile('\.png$')):
		file = link.get('src')
		filename = file.split('/')[-1]
		if file[0] == "/":
			urlretrieve('http://www1.eere.energy.gov' + file, filename)
			print 'http://www1.eere.energy.gov' + file
		else:
			urlretrieve(file, filename)
			print file

if __name__ == "__main__":
	for url in URLs:
		soup = BeautifulSoup(urlopen(url))
		pdfs()
		jpg()
		png()
		excel()
		docs()
