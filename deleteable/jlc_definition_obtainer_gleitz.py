#
# Great work so far!
# I've included some edits in this file to
# help make your code a little more clean.
#

import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib2
import sys


def user_input():
    word = raw_input('What would would you like to be defined?' + '\n')
    if(word == ''):
        sys.exit('you have exited definition_bot')
    return word

def obtain_url(word):
    # Take a look at how a web browser finds the definition of a word with a space in it,
    # e.g. "jungle gym". It converts it to "jungle%20gym" which is called escaping or quoting
    # the text. For more info see http://docs.python.org/library/urllib.html#urllib.quote
    # Try the urllib2.quote function on phrases with weird characters like &, *, ', and #
    url = 'http://www.abbreviations.com/services/v1/defs.aspx?tokenid=tk1765&word=' + urllib2.quote(word)
    response = urllib2.urlopen(url) #opening the url variable
    html = response.read()
    parsed_url = BeautifulStoneSoup(html)
        # To see what this looks like: print parsed_url.prettify() + '\n' + '\n'
    return parsed_url

# This function is for finding the FIRST definition
def find_definition(parsed_url):
    tagfinder = parsed_url.find('definition')
    definition = tagfinder.renderContents()
        # to see what is returned use: print 'the definition of your word is' + ' ' + final
    return definition

# This function is for finding ALL definitions
# This one is not in the main function yet. Must find out how to return all definitions. maybe as arry or list
def find_multiple_definitions(parsed_url):
    multipletagfinder = parsed_url.findAll('definition')
    print '\n'
    for tag in multipletagfinder:
        print tag.renderContents() + '\n--------------------------------------------------'
    print '\n'

def more_definitions_prompt(parsed_url):
    more_definitions_reply = raw_input('would you like more definitions of this word? (y, n)' + '\n')
    if(more_definitions_reply == 'yes') or (more_definitions_reply == 'y'):
        find_multiple_definitions(parsed_url)

def reset():
    main()

##############################################################
#################### MAIN FUNCTION ###########################
##############################################################

def main():
    # Rather than all the rested calls to reset, just put the main function in a loop
    while True:
        word = user_input()
        try:
            parsed_url = obtain_url(word)
            definition = find_definition(parsed_url)
            print '\n' + definition + '\n\n'
            more_definitions_prompt(parsed_url)
        except AttributeError:
            print "Sorry Couldn't find that word! I only know words in the dictionary!" + '\n'
        #except AttributeError == '':
        #    print "Unknown Error.. Resetting.." + '\n'
        #This is made to allow the user to exit if they press Return twice. NOT WORKING
        except:
            print "Unknown Error.. Resetting.." + '\n'

#*******calls the main function********#
# This causes the main function to only be run if you type "python jlc_definition_obtainer"
# If you open the Python console and type "import jlc_definition_obtainer" the main function
# will not be run. This is useful for testing purposes and is the "standard" way to start a program
if __name__ == "__main__":
    main()
