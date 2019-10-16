#Pull tweets from Twint by searched term
#Only get the text from the tweets, store in pandas dataframe.
#TURNED OFF console display of full search. Printed out datafram instead.
#will work on getting this working with TextBlob

import twint

c = twint.Config()
c.Limit = 200
c.Search = "boulder"
c.Format = "Tweet: {tweet}"
# c.Username = username
c.Pandas = True
c.Hide_output = True

twint.run.Search(c)

Tweets_df = twint.storage.panda.Tweets_df
print(Tweets_df.head())
print(Tweets_df.tweet.to_string(index=False))
