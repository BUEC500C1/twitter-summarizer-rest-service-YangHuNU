import os
import pytest
import json
import queue
import threading
from twitter_ import twitter_info
from main import twit_to_image, twit_to_image_no_key

if os.path.exists('./keys'):
	def test_thread1():
		try: 
			q = queue.Queue(maxsize=1)
			# Fetch API keys
			ti = twitter_info('keys')
			q.put("Animals")
			# Get and convert tweets to image
			t2 = threading.Thread(name="Tweets to image", target=twit_to_image, args=(q,ti,1,))
			t2.daemon = True
			t2.start()
			q.join()
		except():
			assert 0
		else:
			assert 1

	def test_thread2():
		try: 
			q = queue.Queue(maxsize=1)
			# Fetch API keys
			ti = twitter_info('keys')
			q.put("Animals")
			# Get and convert tweets to image
			t2 = threading.Thread(name="Tweets to image", target=twit_to_image, args=(q,ti,1,))
			t2.daemon = True
			t2.start()
			q.join()
		except():
			assert 0
		else:
			assert 1

	def test_thread3():
		try: 
			q = queue.Queue(maxsize=1)
			# Fetch API keys
			ti = twitter_info('keys')
			q.put("Animals")
			# Get and convert tweets to image
			t2 = threading.Thread(name="Tweets to image", target=twit_to_image, args=(q,ti,1,))
			t2.daemon = True
			t2.start()
			q.join()
		except():
			assert 0
		else:
			assert 1
		
	def test_tread4():
		try: 
			q = queue.Queue(maxsize=1)
			# Fetch API keys
			ti = twitter_info('keys')
			q.put("Animals")
			# Get and convert tweets to image
			t2 = threading.Thread(name="Tweets to image", target=twit_to_image, args=(q,ti,1,))
			t2.daemon = True
			t2.start()
			q.join()
		except():
			assert 0
		else:
			assert 1

else:
	def test_no_key():
		with open('tweets.json') as f:
			thread_num = 4
			data = json.load(f)
		try: 
			q = queue.Queue(maxsize=4)
			for i in range(thread_num):
				q.put(data[str(i)])
			# Get and convert tweets to image
			for i in range(thread_num):
				t2 = threading.Thread(name="Tweets to image", target=twit_to_image_no_key, args=(q,i,))
				t2.daemon = True
				t2.start()
			q.join()
		except():
			assert 0
		else:
			assert 1