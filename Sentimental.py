import tweepy
from textblob import TextBlob

consumer_key = '' #Remove the consumer_key for security reason
consumer_secret = ''#Remove the consumer_secret for security reason

access_token = ''#Remove the access_token for security reason
access_token_secret = ''#Remove the access_token_secret for security reason

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Narender Modi')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
