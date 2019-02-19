#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 00:41:30 2019
@Credits: https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/
@Credits: http://adilmoujahid.com/posts/2014/07/twitter-analytics/
@author: apurvamodi
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests

ckey = 'mtDSeNYtJUZkKfspxTFmk7Nn8'
csecret = 'iYg5kksoIQKGsXVwGZ7bYpH0cFlxonNPg9hyhDKdGoP89bic6G'
atoken = '1094978973245812738-msYR1atvDnyfTTO46shWdnp5SIJcAA'
asecret = 'EMdqw7fA4IfkDYzKBqNQfoe5sAwz7dgCcRTWkpZOteUKd'
count = 0
uniqueLink = set([])
txtFile = open("tweetURIs.txt","w")
class listener(StreamListener):

    def on_data(self, data):
        global count;
        if(count == 2000):
            return False
        else:
            jsonTweets = json.loads(data)
            links = jsonTweets['entities']['urls']

        if( len(links) != 0 and jsonTweets['truncated'] == False ):
            links = self.getLinksFromTweet(links)
                
            for link in links:
                global uniqueLink
                if(link in uniqueLink):
                    pass
                else:
                    print(link)
                    count = count + 1
                    uniqueLink.add(link)
                    txtFile.write(link)
                    txtFile.write('\n')
            #print(count)
        return True

    def getLinksFromTweet(self, linksDict):

        links = []
        destUrl = ''
        for uri in linksDict:

            if("https://twitter.com" in uri['expanded_url']):
                pass
            else:
                destUrl = self.checkForRedirection(uri['expanded_url'][0:])
                links.append(destUrl)
            return links

    def checkForRedirection(self,link1):
        response = requests.get(link1, allow_redirects=False, timeout=5)
        return response.url



    def on_error(self, status):
        if status == 420:
            #returning False in on_data disconnects the stream
            return False
        return True
    

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
try:
  twitterStream = Stream(auth, listener())
  twitterStream.filter(track=['crypto'])
except:
  twitterStream.filter(track=['crypto'])
txtFile.close()



