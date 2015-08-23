import sys
import os
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import time
from threading import Thread
from multiprocessing import Process

# INSTRUCTIONS : Modify the threadcount[] list with no of threads to test

def getxkcd(id):
	url='http://xkcd.com/%d' %id
	page=urllib.request.urlopen(url)

	soup=BeautifulSoup(page.read())	
	page.close();

	div=soup.findAll('div',attrs={'id':'comic'})

	for link in div:
		l=link.findAll('img')
		for x in l:
			yay='http:'+x['src']

	if not os.path.exists('xkcd/'):
		os.makedirs('xkcd/')
	urllib.request.urlretrieve(yay, 'xkcd/%d.jpg' %id)
	#print('%d downloaded' %id)
	return id+1


def xkcddownloadingthread(start,increment,limit):  # Uncomment all print statements for verbose mode (good for shitty connections)
	cur=start   
	while(cur<limit):
		while True:
			try:
				#print(start," is downloading ",cur)
				getxkcd(cur)
			except:
				#print("Failed to get ",cur)
				continue
			else:
				#print(start, " downloaded ",cur)
				break
		cur=cur+increment

		 
def serialaverage(nooftries):  # Pass the number of test cases for each process count that is averaged
	threadcount=[8] # Enter the process counts that you want it to check 
	for j in threadcount:
		etime=0
		for s in range(1,nooftries+1):
			threads=[]
			start=time.time()
			for i in range(1,j+1):
				t=Thread(target=xkcddownloadingthread,args=(i,j,100,))
				threads += [t]
				t.start()
			for x in threads:
				x.join()
			end=time.time()
			print("Thread count :",j," round ",s," time : ",end-start)
			etime=etime+end-start
		print("Thread Count :",j,"Average :",etime/3)

def parallelaverage(nooftries): # Pass the number of test cases for each process count that is averaged
	threadcount=[8,12] # Enter the process counts that you want it to check 
	etime={}
	for i in threadcount:
		etime[i]=0;
	for i in range(1,nooftries+1):
		for j in threadcount:
			start=time.time()
			threads=[]
			for k in range(1,j+1):
				t=Thread(target=xkcddownloadingthread,args=(k,j,100,))
				threads+=[t]
				t.start()
			for x in threads:
				x.join()
			end=time.time()
			print("Thread count",j," Round ",i," time :",end-start)
			etime[j]+=end-start
	for i in threadcount:
		print("Thread count :",i," Average: ",etime[i]/nooftries)

