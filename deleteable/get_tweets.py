import tweepy
import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib2
import urllib
import simplejson
import json

def get_tweet():
    username = "a_Olafsson"     #"DefinitionBot"
    url = 'http://search.twitter.com/search.json?q=@' + username
    response = urllib2.urlopen(url)
    html = response.read()
    json_response = simplejson.load(urllib.urlopen(url))
    test_results = json_response['results'] #It obtains the key value 'results' from the dict result.
    print test_results[0]['text'] #obtains key value text from within results.

