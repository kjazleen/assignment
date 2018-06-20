
#Q1 (i)  what is access token?
#An access token is an object that describes the security context of a process or thread.

#How generate your access token for any API?
#sign in to developer account
#creat a new api
#under that go to keys and access token
#generate access token



#Q2
#google IP address=172.217.15.68
#facebook IP address=31.13.69.230


#Q3
'''import tweepy
from keys import consumer_key,consumer_secret,access_secret,access_token


oauth=tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_secret)
api=tweepy.API(oauth)
print(api.search("#modi"))'''

#Q4
#API:
# API is a part of library which defines how an application communicates with external code.
# API can be written in any language.
#Library:
# Library is written in same language which is a collection of all the functionalities required for the use case.
#For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along
#with a large collection of high-level mathematical functions to operate on these arrays.")

#Q5
'''import tweepy
import keys import consumer_key,consumer_secret,acess_secret,acess_token

outh=tweepy.OAuthHandler(consumer_key,consumer_secret)
outh.set_access_token(access_token,acess_secret)
api=tweepy.API(oauth)
user=api.get_user("@kaurjazleen2")
print(user.screen_name)
print(user.freinds_count)
print(user.followers_count)'''