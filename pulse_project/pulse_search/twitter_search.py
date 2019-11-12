import sys
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
	def __init__(self):

		consumer_key = 'redacted'
		consumer_secret = 'redacted'
		access_token = 'redacted'
		access_token_secret = 'redacted'

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

def main(search_term):
	api = TwitterClient()
	tweets = api.get_tweets(query = search_term, count = 10)

	# ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	# print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
	# ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	# print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	# print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))

	print("tweets collected: ", len(tweets))
	tweet_dict2 = []
	for tweet in tweets:
		tweet_dict2.append(tweet['id'])
	tweets_dict = (
	{
	    'id' : tweet_dict2[0],
	    'index' : '1'
	},
	{
	    'id' : tweet_dict2[1],
	    'index' : '2'
	},
	{
        'id' : tweet_dict2[2],
	    'index' : '3'
	},
	{
	    'id' : tweet_dict2[3],
	    'index' : '4'
	},
	{
	    'id' : tweet_dict2[4],
	    'index' : '5'
	},
	{
	    'id' : tweet_dict2[5],
	    'index' : '6'
	},
	{
	    'id' : tweet_dict2[6],
	    'index' : '7'
	},
	{
	    'id' : tweet_dict2[7],
	    'index' : '8'
	},
	{
	    'id' : tweet_dict2[8],
	    'index' : '9'
	},
	{
	    'id' : tweet_dict2[9],
	    'index' : '10'
	}
	)

	return tweets_dict
