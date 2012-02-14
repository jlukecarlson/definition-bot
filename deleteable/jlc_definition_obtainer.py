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
    url = 'http://www.abbreviations.com/services/v1/defs.aspx?tokenid=tk1765&word=' + word
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
    for tag in multipletagfinder:
        print tag.renderContents() + '\n'
        
def more_definitions_prompt(parsed_url):
    more_definitions_reply = raw_input('would you like more definitions of this word? (y, n)' + '\n')
    if(more_definitions_reply == 'yes') or (more_definitions_reply == 'y'):
        more_definitions = find_multiple_definitions(parsed_url)
        reset()
    else:
        reset()
def reset():
    main()

##############################################################
#################### MAIN FUNCTION ###########################
##############################################################

def main():
    word = user_input()
    try:
        parsed_url = obtain_url(word)
        definition = find_definition(parsed_url)
        print definition + '\n'
        more_definitions_prompt(parsed_url)
    except AttributeError:
        print "Sorry Couldn't find that word! I only know words in the dictionary! Resetting..." + '\n'
        reset()
    #except AttributeError == '':
    #    print "Unknown Error.. Resetting.." + '\n'
    #This is made to allow the user to exit if they press Return twice. NOT WORKING
    except:
        print "Unknown Error.. Resetting.." + '\n'
        reset()

#*******calls the main function********#
main()
