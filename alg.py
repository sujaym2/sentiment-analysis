from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string

class alg():
    def percentage(part,whole):
 return 100 * float(part)/float(whole)keyword = input(“Please enter keyword or hashtag to search: “)
 noOfTweet = int(input (“Please enter how many tweets to analyze: “))tweets = tweepy.Cursor(api.search, q=keyword).items(noOfTweet)
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []for tweet in tweets:
 
 #print(tweet.text)
 tweet_list.append(tweet.text)
 analysis = TextBlob(tweet.text)
 score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
 neg = score[‘neg’]
 neu = score[‘neu’]
 pos = score[‘pos’]
 comp = score[‘compound’]
 polarity += analysis.sentiment.polarity
 
 if neg > pos:
 negative_list.append(tweet.text)
 negative += 1elif pos > neg:
 positive_list.append(tweet.text)
 positive += 1
 
 elif pos == neg:
 neutral_list.append(tweet.text)
 neutral += 1positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, ‘.1f’)
negative = format(negative, ‘.1f’)
neutral = format(neutral, ‘.1f’)

tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print(“total number: “,len(tweet_list))
print(“positive number: “,len(positive_list))
print(“negative number: “, len(negative_list))
print(“neutral number: “,len(neutral_list))

def count_values_in_column(data,feature):
 total=data.loc[:,feature].value_counts(dropna=False)
 percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
 return pd.concat([total,percentage],axis=1,keys=[‘Total’,’Percentage’])#Count_values for sentiment
count_values_in_column(tw_list,”sentiment”)

