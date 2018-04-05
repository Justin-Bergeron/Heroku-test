# Dependencies
import numpy as np
import tweepy
import time
import json
#from config import consumer_key, consumer_secret, access_token, access_token_secret

# Twitter API Keys
consumer_key = "GvauzqzfE2o1eqIHxk5X8q38u"
consumer_secret = "cBfUvQ37EbQKPP2FjyhqVxTyCrBqnlEa8bts81C5SWOUDxpXsA"
access_token = "980991539739484160-jivEu1NrRKe7rLsHr3ZBBf2YRtYSWab"
access_token_secret = "GPcMoprjKx5D7lhvA3Xj10diRnhcHBLsowELyfE1EuoHN"
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create Thank You Function
def ThankYou():
    
    # Target User
    target_term = "bobbobe37676119"
    
    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Search for all tweets
    public_tweets = api.search(target_term, count=100, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets['statuses']:

        # Get ID and Author of most recent tweet directed to me
        tweet_id = tweet["id"]
        tweet_author = tweet["user"]["screen_name"]
        tweet_text = tweet["text"]
        # Print the tweet_id


        # Use Try-Except to avoid the duplicate error
    try:
        api.update_status(f'Hey {tweet_author} thanks for the friendlies')  
    except Exception:
        print('we already thanked them')

ThankYou()        