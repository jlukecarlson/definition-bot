# the big papa main function
import time
import pickle
import grab_definition as define
import grab_tweet as gtweet
import post_tweet as ptweet

def test():
    words = gtweet.get_text()
    print words

def main():
    tweet_file = open('tweets.backup', 'r')
    responded_tweets = pickle.load(tweet_file)
    tweet_file.close()
    while True:
        word = gtweet.get_text()
        definition = define.grab_definition(word)
        user= gtweet.get_user()
        if word not in gtweet.responded_tweets:
            ptweet.post_tweet(user, word, definition)
            responded_tweets.append(word)
            # write responded tweets to a file
        else:
            pass
        time.sleep(60)
