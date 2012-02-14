#Gets tweets from an account. we need to do try catches for errors later
import tweepy
import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib2
import urllib
import simplejson
import json

# List of tweets that have already been responded to
responded_tweets = []

def grab_tweet():
    url = 'http://search.twitter.com/search.json?q=@DefinitionBot'
    response = urllib2.urlopen(url)
    html = response.read()
    json_response = simplejson.load(urllib.urlopen(url))
    api_results = json_response['results'] #It obtains the key value 'results' from the dict result.
    return api_results

def get_user():
    api_results = grab_tweet()
    user =  api_results[0] ['from_user'] #returns key value from_user from within results.
    return user
    

def get_text():
    api_results = grab_tweet()
    words = []
    for i in range(0, 3):
        #if(word in words):
            
        tweet =  api_results[i]['text'] #returns key value text from within results.
        word = tweet[15:150] #splicing
        words.append(word)
        #print word
        i += 1
        
    return words
 
