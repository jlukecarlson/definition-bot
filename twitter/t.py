import os, sys
import time
import datetime

import simplejson
import twitter

if __name__ == '__main__':
    # #debug:
    # api      = twitter.Api(username='GDdmIQH6jhtmLUypg82g',
    #                        password='MCD8BKwGdgPHvAuvgvz4EQpqDAtx89grbuNMRd7Eh98',
    #                        access_token_key='819797-Jxq8aYUDRmykzVKrgoLhXSq67TEa5ruc4GJC2rWimw',
    #                        access_token_secret='J6zix3FfA9LofH0awS24M3HcBYXO5nI1iYe8EfBA',
    #                        use_gzip_compression=True)

    #bear:
    api      = twitter.Api(consumer_key='IssiRNt8rssXfHrcloGulg',
                           consumer_secret='0i7NpqPiBi2IvXCTIX51hEXMxiL1NSsj7ciFiJYhKs',
                           access_token_key='16133-ca1B0p3olYdKRIdMX1RbrVBfK34x4Be0yRh3Sjaeg',
                           access_token_secret='8tyQi2NfKn6TecWHPIQOU1wCFgdRVCA6U8Z6lWGRY3w',
                           debugHTTP=True)

    print api.VerifyCredentials()


    since_id = None
    # try:
    #     print '-+'*10, 'polling Public Timeline'
    #     for status in api.GetPublicTimeline(since_id=since_id):
    #         item = status.AsDict()
    #         print item
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Friends Timeline'
    #     for status in api.GetFriendsTimeline(retweets=False):
    #         item = status.AsDict()
    #         print item
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Home Timeline'
    #     for status in api.GetFriendsTimeline(retweets=True):
    #         item = status.AsDict()
    #         print item
    # finally:
    #     print '*'*50
    
    try:
        print '-+'*10, 'User Timeline'
        for status in api.GetUserTimeline():
            item = status.AsDict()
            print item
    finally:
        print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Favorites'
    #     for status in api.GetFavorites():
    #         item = status.AsDict()
    #         print item
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Mentions'
    #     for status in api.GetMentions():
    #         item = status.AsDict()
    #         print item
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Retweets by User'
    #     for status in api.GetUserRetweets():
    #         item = status.AsDict()
    #         print item
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Lists'
    #     for status in api.GetLists('manta'):
    #         item = status.AsDict()
    #         print item
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Post Test'
    #     api.PostUpdate('Testing oAuth from command line %s' % time.time())
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Post Test - unicode'
    #     s = '\xE3\x81\x82' * 10
    #     api.PostUpdate('%s %s' % (s, time.time()))
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'Post Test - unicode'
    #     s = '\u1490'
    #     api.PostUpdate('%s %s' % (s, time.time()))
    # finally:
    #     print '*'*50
    # try:
    #     print '-+'*10, 'Post Test - unicode'
    #     # make sure input encoding param is set
    #     s = u'\u3042' * 10
    #     api.PostUpdate(u'%s %s' % (s, time.time()))
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'destroy friendship link'
    #     print api.DestroyFriendship("coda").AsDict()
    # finally:
    #     print '*'*50
    # 
    # try:
    #     print '-+'*10, 'create friendship link'
    #     print api.CreateFriendship("coda").AsDict()
    # finally:
    #     print '*'*50



