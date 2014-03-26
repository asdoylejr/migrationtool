from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv
import re

class Tracker():
    def __init__(self):
        pass

    def create_tracker(self):
        URLS = open("trackerurls.txt").readlines()

        with open('tracker.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for url in URLS:
                if url[-5:] != 'html\n':
                    writer.writerow([url, 'ERROR'])
                    continue
                try:
                    html_data = urlopen(url)
                    print('Successfully opened %s' % url)
                except:
                    print('Error opening URL: ' + url)
                    writer.writerow([url, 'ERROR'])

                soup = bs(html_data)
                header = soup.find('h1')
                header_final = re.sub('')
                writer.writerow([url, headertag])
                print('Row successfully written for %s' % url)

def main():

    bot = Tracker()
    bot.create_tracker()

    #create_tracker()
    
if __name__ == "__main__":
    main()
