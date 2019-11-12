#Run with:
# python3 tweepy_test.py search term here
#ex: python3 tweepy_test.py cu boulder

import sys
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
	def __init__(self):

		# consumer_key = 'redacted'
		# consumer_secret = 'redacted'
		# access_token = 'redacted'
		# access_token_secret = 'redacted'
		consumer_key = 'bVgAX5fGidoy2IgPKHHgcfOG4'
		consumer_secret = '83b6zN5HSIjPk7ALaGwcFY9DRwNEvOABgB0YD3TJI4KXigzJY9'
		access_token = '48478289-5oNed2t3pcbO5aSt5DdeoeoOTfLUePQUYJ96tkkfd'
		access_token_secret = 'VDOFj9IjC0r5QgbIu1kGgAp68fEwHjKLlhGJkBPFRNbXD'

		try:
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token, access_token_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def get_tweet_sentiment(self, tweet):
		analysis = TextBlob(self.clean_tweet(tweet))
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def get_tweets(self, query, count = 50):
		tweets = []
		try:
			fetched_tweets = self.api.search(q = query, count = count)

			for tweet in fetched_tweets:
				parsed_tweet = {}
				parsed_tweet['text'] = tweet.text
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
				parsed_tweet['id'] = tweet.id
				if tweet.retweet_count > 0:
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			return tweets

		except tweepy.TweepError as e:
			print("Error : " + str(e))

def main(argv, argsLen):
	if(argsLen <= 1):
		print("No search term included on the command line!")
		return

	term = ""
	for i in range(0, argsLen-1):
		if i != 0:
			term += " "
			term += argv[i]
		else:
			term += argv[i]
	print("Searching for: ",term)

	api = TwitterClient()
	tweets = api.get_tweets(query = term, count = 10)

	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))

	print("tweets collected: ", len(tweets))
	for tweet in tweets:
		print(tweet['id'])


if __name__ == "__main__":
	# calling main function\
	main(sys.argv[1:], len(sys.argv))
