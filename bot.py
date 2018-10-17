import tweepy
import requests
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
data1 = "Joke of the Day\n"
data2 = requests.get('https://api.yomomma.info/').json()["joke"]
# import pdb; pdb.set_trace()
api = tweepy.API(auth)
# print(data1+" "+data2)
# print(api.status_code)
api.update_status(status=data1+data2)