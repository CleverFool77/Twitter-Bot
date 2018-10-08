import tweepy
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
# import pdb; pdb.set_trace()
api = tweepy.API(auth)
# print(api.status_code)
api.update_status(status="checking twitter bot update")