import sys
import os

import urllib

import HTMLParser
from bs4 import BeautifulSoup
import json

'''
Instructions for writing a scraper for a given site:

The algorithm for scraping a given site can be described as follows:
1. Generate the URL of the comic's page given the ID
2. Send a request to the URL and get the HTML page
3. Soupify the page using BeautifulSoup
4. Get the required image tag from the soup and obtain the image URL
5. Download the image from the URL and write into the corresponding comic folder

Step 1 and 4 alone have to be implemented by the user in the custom function
Steps 2, 3 and 5 are implemented automatically in the above system.

To scrape an entire site, a method to determine the next page must be specified.
'''

# Algorithm implementation
def scrape_page(url, id, scrape_image, image_path):
	# Step 2
	page = urllib.urlopen(url)

	# Step 3
	page_soup = BeautifulSoup(page.read())	
	page.close()

	# Step 4
	image_url = scrape_image(page_soup)

	# Step 5
	if not os.path.exists(image_path + '/'):
		os.makedirs(image_path + '/')
	extension = image_url.split('.')[-1]
	urllib.urlretrieve(image_url, '%s/%s.%s' % (image_path, id, extension))


def getXKCD(id):
	url = 'http://xkcd.com/%d' %id
	
	def scrape_image(soup):
		div = soup.find('div',attrs={'id':'comic'})
		image = div.find('img')
		image_url='http:'+image['src']
		return image_url

	scrape_page(url, id, scrape_image, 'xkcd')
	print('%d downloaded' %id)

	# Get next ID
	return id+1


def getDogHouseDiaries(id):
	url='http://thedoghousediaries.com/%d' %id

	def scrape_image(soup):
		div = soup.find('div',attrs={'id':'imgdiv'})
		link = div.find('img')
		image_url='http://thedoghousediaries.com/'+link['src']
		return image_url

	scrape_page(url, id, scrape_image, 'doghousediaries')

	print('%d downloaded' %id)

	# Get next ID
	next = soup.find('a', {'id':'nextlink'})
	next = next['href']
	next = next[-2:]
	next = int(next)
	return next


def getSaturdayMorningBreakfastCereal(id):
	url='http://www.smbc-comics.com/index.php?id=%d' %id

	def scrape_image(soup):
		image = soup.find('img',{'id':'comic'})
		image_source = image['src']
		image_url = 'http://www.smbc-comics.com/'+image_source
		return image_url

	scrape_page(url, id, scrape_image, 'smbc')
	print('%d downloaded' %id)
	# Get next ID
	
	return id + 1


def getCyanideAndHappiness(id):
	url='http://explosm.net/comics/%d' %id

	def scrape_image(soup):
		image = soup.find('img',{'id':'main-comic'})
		image_source = image['src']
		image_url = 'http:' + image_source
		return image_url

	scrape_page(url, id, scrape_image, 'cyanideandhappiness')

	print('%d downloaded' %id)

	# get next ID


def getChannelate(url):
	# Specify URL here

	def scrape_image(soup):
		# Implement scrape image here
		return image_url
pass


def getPHDComics(id):
	# Specify URL here

	def scrape_image(soup):
		# Implement scrape image here
		return image_url	
	pass
