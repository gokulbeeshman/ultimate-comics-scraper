import Scraper
import time

from threading import Thread

# Set to 'False' to disable logs
ENABLE_LOGGING = True

# A logging function that will print logs if
def log(message):
	if ENABLE_LOGGING == True:
		print message

def downloadThread(webcomic_function, start, limit, step):
	try:
		map(webcomic_function, range(start, limit, step))
	except:
		log("Downloader failed")

# Assuming the default processor to be a dual core
def parallelAverage(webcomic_function, no_of_tries=1, thread_counts=[4]):
	for thread_count in thread_counts:
		execution_time = 0
		for i in range(0, no_of_tries):
			executing_threads = []
			start_time = time.time()
			for j in range(0, thread_count):
				thread = Thread(target=downloadThread, args=(webcomic_function,j, 100, thread_count)) 
				executing_threads += [thread]
				thread.start()

			for thread in executing_threads:
				thread.join()
			end_time = time.time()
			print "Thread Count: %d; Attempt: %d; Execution Time: %s" % (thread_count, i, (end_time - start_time))
			execution_time = execution_time + (end_time - start_time)
		print "Thread Count: %d; Average time: %d" % (thread_count, execution_time/no_of_tries)
