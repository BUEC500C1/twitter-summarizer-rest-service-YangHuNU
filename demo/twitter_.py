import tweepy
import os
import configparser
import json

class twitter_info():
	def __init__(self, path):
		config = configparser.ConfigParser()
		config.read(path)
		auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
		auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_secret').strip())
		self.api = tweepy.API(auth)

	def getting_pics(self, screen_name):
		alltweets = []
		new_tweets = self.api.user_timeline(screen_name = screen_name, count=3)
		alltweets.extend(new_tweets)

		result = ''

		for status in alltweets:
			if hasattr(status, "retweeted_status"):
				try:
					result += status.retweeted_status.extended_tweet["full_text"]
					result += "\n------\n"
				except(AttributeError):
					result += status.retweeted_status.text
					result += "\n------\n"
			else:
				try:
					result += status.extended_tweet["full_text"]
					result += "\n------\n"
				except(AttributeError):
					result += status.text
					result += "\n------\n"
		return result


if __name__ == "__main__":
	n = twitter_info("keys")
	lis = []
	lis.append(n.getting_pics("Friends"))
	lis.append(n.getting_pics("Animals"))
	lis.append(n.getting_pics("Penguins"))
	lis.append(n.getting_pics("Lions"))
	d = enumerate(lis)
	with open("tweets.json","w+") as f:
		json.dump(dict(d),f)
	print(n.getting_pics("Friends"))
	print(n.getting_pics("Animals"))
	print(n.getting_pics("Penguins"))
	print(n.getting_pics("Lions"))
	print(n.getting_pics("Tigers"))
	print(n.getting_pics("Cats"))
	print(n.getting_pics("Dogs"))