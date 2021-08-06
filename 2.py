#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install tweepy


# In[6]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = 
csecret = 
atoken = 
asecret = 
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin_luis:audelfy232A@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('juegos_olimpicos')
except:
    db = server['juegos_olimpicos']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[1.1903,46.4431,3.1229,47.3109])  
twitterStream.filter(track=['juegosolimpicos','medallista'])


# In[ ]:




