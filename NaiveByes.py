#Importing Libraries
import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
# from wordcloud import WordCloud
import json
from collections import Counter



#Authorization and Search tweets
#Getting authorization
consumer_key = 'mNZyUpMnwuRs4QNw6zgPD2GBO'
consumer_key_secret = 'iXJXirFEiZsAvF9FVC7DwYZVVBDoT2NYYQ3soHuyckQFuQhRkV'
access_token = '3112006849-Oa9h7tKeeHIur17R4otVaDFgzTspaYxLHJg1Pzl'
access_token_secret = '3z8FqQ23pWSZHH6GoEe2IDZodf2k7lVEchIOmk97odeXl'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
