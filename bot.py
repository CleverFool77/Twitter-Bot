import tweepy
import requests
consumer_key = os.environ.get(consuner_key) 
consumer_secret = os.environ.get(consuner_secret) 
access_token = os.environ.get(access_token) 
access_token_secret = os.environ.get(access_token_secret)

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
data1 = "Joke of the Day\n"
data2 = requests.get('https://api.yomomma.info/').json()["joke"]
# import pdb; pdb.set_trace()
api = tweepy.API(auth)
# print(data1+" "+data2)
# print(api.status_code)
api.update_status(status=data1+data2)
