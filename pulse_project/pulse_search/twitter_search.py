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

	def get_tweets(self, query, count):
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

def main(search_term):
	api = TwitterClient()
	tweets = api.get_tweets(query = search_term, count = 200)

	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	# print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	# print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	# print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))

	# print("tweets collected: ", len(tweets))

	tweet_ids = []
	sentiment_dict = {
		'positive' : 100*len(ptweets)/len(tweets),
		'negative' : 100*len(ntweets)/len(tweets),
		'neutral' : 100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets),
		'size' : len(tweets)
	}
	for tweet in tweets:
		tweet_ids.append(tweet['id'])

	tweets_dict = []
	for i in range(0, len(tweet_ids)):
		tweet = {}
		tweet['id'] = tweet_ids[i]
		tweet['index'] = i+1
		tweets_dict.append(tweet)


	return (tuple(tweets_dict), sentiment_dict)
