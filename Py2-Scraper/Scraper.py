import sys
import os

import urllib

import HTMLParser
from bs4 import BeautifulSoup
import json

class ComicScraper():
	def make_soup(self, url):
		page = urllib.urlopen(url)
		soup = BeautifulSoup(page.read())	
		page.close()
		return soup

	def download_file(self, image_url, id, path):
		if not os.path.exists(path + '/'):
			os.makedirs(path + '/')
		extension = image_url.split('.')[-1]
		urllib.urlretrieve(image_url, '%s/%s.%s' % (path, id, extension) ) 

	def getXKCD(self, id):
		url = 'http://xkcd.com/%d' %id

		soup = self.make_soup(url)

		# Comic URL Scraping here
		div = soup.find('div',attrs={'id':'comic'})
		image = div.find('img')
		image_url='http:'+image['src']

		self.download_file(image_url, id, 'xkcd')

		print('%d downloaded' %id)

		# Get next ID
		return id+1

	def getDogHouseDiaries(self, id):
		url='http://thedoghousediaries.com/%d' %id

		soup = self.make_soup(url)

		# Comic URL Scraping here
		div = soup.find('div',attrs={'id':'imgdiv'})
		link = div.find('img')
		image_url='http://thedoghousediaries.com/'+link['src']

		self.download_file(image_url, id, 'doghouse')

		print('%d downloaded' %id)

		# Get next ID
		next = soup.find('a', {'id':'nextlink'})
		next = next['href']
		next = next[-2:]
		next = int(next)
		return next

	def getSaturdayMorningBreakfastCereal(self, id):
		url='http://www.smbc-comics.com/index.php?id=%d' %id
		
		soup = self.make_soup(url)

		# Comic URL Scraping here
		image = soup.find('img',{'id':'comic'})
		image_source = image['src']
		image_url = 'http://www.smbc-comics.com/'+image_source

		self.download_file(image_url, id, 'smbc')

		print('%d downloaded' %id)

		# Get next ID
		return id + 1

	def getCyanideAndHappiness(self, id):
		url='http://explosm.net/comics/%d' %id
		
		soup = self.make_soup(url)

		# Comic URL Scraping here
		image = soup.find('img',{'id':'main-comic'})
		image_source = image['src']
		image_url = 'http:' + image_source

		self.download_file(image_url, id, 'cyanideandhappiness')

		print('%d downloaded' %id)

		# get next ID

	def getchannelate(url):
		pass


	def getphdcomics(id):
		pass
