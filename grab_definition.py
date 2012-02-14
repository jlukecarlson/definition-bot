#Final definition grabber

import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib2
import sys

def obtain_url(word):
    url = 'http://www.abbreviations.com/services/v1/defs.aspx?tokenid=tk1765&word=' + urllib2.quote(word)
    #encodes the input allowing for definitions of multi-word terms
    response = urllib2.urlopen(url) #opening the url variable
    html = response.read()
    parsed_url = BeautifulStoneSoup(html)
    return parsed_url

def find_definition(parsed_url):
    tagfinder = parsed_url.find('definition')
    definition = tagfinder.renderContents()
    return definition

def grab_definition(word):
 while True:
        try:
            parsed_url = obtain_url(word)
            definition = find_definition(parsed_url)
            return definition
        except AttributeError:
            return "Sorry Couldn't find that word! I only know words in the dictionary! Resetting..."
        except:
            return "Unknown Error.. Resetting.."
## above should be the big boy main


#def main():
#    while True:
#        word = user_input()
#        try:
#            parsed_url = obtain_url(word)
#            definition = find_definition(parsed_url)
#            return definition
#        except AttributeError:
#            print "Sorry Couldn't find that word! I only know words in the dictionary! Resetting..." + '\n'
#        except:
#            print "Unknown Error.. Resetting.." + '\n'

#runs the main
#if __name__ == "__main__":
#    main()

j = "hahjshja"
