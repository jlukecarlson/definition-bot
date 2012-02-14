#posts the tweet with arguments PASSED INTO THE FUNCTION
import sys
import tweepy
import twitter

CONSUMER_KEY = 'UaIo7UWWD3hzIO0NKvAA'
CONSUMER_SECRET = 'Q4yyOVMHRVoFke5M9x2GQDMYy9cv8nfrJ3WaHGVK8Yg'
ACCESS_KEY = '427037319-Bud9ECEkODWJ8Oi9Furea9Lxtx6EuWtUB7bvPxJr'
ACCESS_SECRET =  'I4mEv7NFuNhrvLs2tSSLDQ4iVLWNHd9LI6pFnL2gZLM'
# these keys are all for authenticating DefinitionBot account.

def post_tweet(user, word, definition):
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        message = '@' + user + " " + word + ": " + definition
        if (message > 140):
            api.update_status("Sorry the definition is too long") # to fit in a tweet")
        else:
            api.update_status('@' + user + " " + word + ": " + definition)
        #api.update_status('@' + user + " " + word + ": " + definition)
    except AttributeError: #tweepy.TweepError: #to catch duplicate message
        print "Dupe status"
#def post_tweet(user, word, definition):
#    try:
#        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#        api = tweepy.API(auth)
#        message = '@' + user + " " + word + ": " + definition
#        if (message < 140):
#            api.update_status("Sorry the definition is too long") # to fit in a tweet")
#        else:
#            api.update_status('@' + user + " " + word + ": " + definition)
#        #api.update_status('@' + user + " " + word + ": " + definition)
#    except AttributeError: #tweepy.TweepError: #to catch duplicate message
#        print "Dupe status"
