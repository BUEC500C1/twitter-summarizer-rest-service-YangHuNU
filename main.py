import queue
import threading
import os
import time
import json

from twitter_ import twitter_info
from text_to_image import generate_image
from images_to_video import generate_video

# Fetch tweets and convert them to image
def twit_to_image(q, ti, counter):
	while(True):
		screen_name = q.get()
		content = ti.getting_pics(screen_name)
		generate_image(content, counter)
		print("Processing "+str(counter)+"thread")
		q.task_done()

# For pytest no key version of twit_to_image
def twit_to_image_no_key(q, counter):
	while(True):
		content = q.get()
		generate_image(content, counter)
		print("Processing"+str(counter)+"thread")
		q.task_done()

# Get user input from command line interface
def get_screen_names(q):
		twit_name = input("Please enter a Twitter user ID: ")
		if twit_name != '':
			q.put(twit_name)


def executing():
	# Establish queue
	q = queue.Queue(maxsize=4)

	thread_num = 4

	# Fetch API keys
	ti = twitter_info('keys')

	for i in range(thread_num):
		get_screen_names(q)

	# Get and convert tweets to image
	for i in range(thread_num):
		t2 = threading.Thread(name="Tweets to image", target=twit_to_image, args=(q,ti,i,))
		t2.daemon = True
		t2.start()
	q.join()

def input_flask(ID0,ID1,ID2,ID3):
	# Establish queue
	q = queue.Queue(maxsize=4)

	thread_num = 4

	# Fetch API keys
	ti = twitter_info('keys')

	q.put(ID0)
	q.put(ID1)
	q.put(ID2)
	q.put(ID3)

	# Get and convert tweets to image
	for i in range(thread_num):
		t2 = threading.Thread(name="Tweets to image", target=twit_to_image, args=(q,ti,i,))
		t2.daemon = True
		t2.start()
	q.join()

def get_video():
	generate_video()

if __name__ == "__main__":
	executing()
	get_video()



