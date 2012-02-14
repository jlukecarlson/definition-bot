import sys
import tweepy
import twitter

CONSUMER_KEY = 'UaIo7UWWD3hzIO0NKvAA'
CONSUMER_SECRET = 'Q4yyOVMHRVoFke5M9x2GQDMYy9cv8nfrJ3WaHGVK8Yg'
ACCESS_KEY = '427037319-Bud9ECEkODWJ8Oi9Furea9Lxtx6EuWtUB7bvPxJr'
ACCESS_SECRET =  'I4mEv7NFuNhrvLs2tSSLDQ4iVLWNHd9LI6pFnL2gZLM'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#api.update_status("test2")
print api.GetUser("DefinitionBot")

