import sys
import os
import urllib.request
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import time
from threading import Thread
from multiprocessing import Process

# INSTRUCTIONS : Modify processcount[] list with no of processes to test with

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


def xkcddownloadingthread(start,increment,limit):
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

		
def serialaverage(nooftries):	# Pass the number of test cases for each process count that is averaged
	processcount=[16] # Enter the process counts that you want it to check 		  	
	for j in processcount:
		etime=0
		for s in range(1,nooftries+1):
			processes=[]
			start=time.time()
			for i in range(1,j+1):
				t=Process(target=xkcddownloadingthread,args=(i,j-1,100,))
				processes += [t]
				t.start()
			for x in processes:
				x.join()
			end=time.time()
			print("Process count :",j," round ",s," time : ",end-start)
			etime=etime+end-start
		print("Process Count :",j,"Average :",etime/nooftries)


def parallelaverage(nooftries): # Pass the number of test cases for each process count that is averaged
	processcount=[12,16] # Enter the process counts that you want it to check 
	etime={}
	for i in processcount:
		etime[i]=0;
	for i in range(1,nooftries+1):
		for j in processcount:
			start=time.time()
			processes=[]
			for k in range(1,j+1):
				t=Process(target=xkcddownloadingthread,args=(k,j,100,))
				processes+=[t]
				t.start()
			for x in processes:
				x.join()
			end=time.time()
			print("Process count",j," Round ",i," time :",end-start)
			etime[j]+=end-start
	for i in processcount:
		print("Process count :",i," Average: ",etime[i]/nooftries)

