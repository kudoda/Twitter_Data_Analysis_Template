import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns
import gensim
from gensim.models import CoherenceModel
from gensim import corpora
import pandas as pd
from pprint import pprint
import string
import os
import re
import numpy as np 
import nltk 



class DataLoader:
  def __init__(self,dir_name,file_name):
    self.dir_name=dir_name
    self.file_name = file_name
    
 
  def read_csv(self):
    os.chdir(self.dir_name)
    tweets_df=pd.read_csv(self.file_name)
    return tweets_df

#object creation
'''
loading the data
'''

#DataLoader_obj= DataLoader('/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template','global_processed_tweet_data.csv')
DataLoader_obj= DataLoader('/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template','africa_processed_tweet_data.csv')
tweets_df=DataLoader_obj.read_csv()
tweets_df.dropna()
print (len(tweets_df))
#print (tweets_df.head())

'''
  #############################vvvvvvvvvvvvcleaning the txt not need for this task
'''
class PrepareData:
  def __init__(self,df):
    self.df=df
    
  def preprocess_data(self):
    tweets_df = self.df.loc[self.df['lang'] =="en"]

    #text Preprocessing
    tweets_df['original_text'] = tweets_df['original_text'].astype(str)
    tweets_df['original_text'] = tweets_df['original_text'].apply(lambda x: x.lower())
    tweets_df['original_text'] = tweets_df['original_text'].apply(lambda x: x.translate(str.maketrans(' ', ' ', string.punctuation)))
   
    #Converting tweets to list of words For feature engineering
    sentence_list = [tweet for tweet in tweets_df['original_text']]
    word_list = [sent.split() for sent in sentence_list]
    # print(word_list)

    #Create dictionary which contains Id and word 
    word_to_id = corpora.Dictionary(word_list) #generate unique tokens
    #  we can see the word to unique integer mapping
    # print(word_to_id.token2id)
    # using bag of words(bow), we create a corpus that contains the word id and its frequency in each document.
    corpus_1= [word_to_id.doc2bow(tweet) for tweet in word_list]
    # TFIDF

    return word_list, word_to_id, corpus_1



PrepareData_obj=PrepareData(tweets_df)
word_list ,id2word,corpus=PrepareData_obj.preprocess_data()
id_words = [[(id2word[id], count) for id, count in line] for line in corpus]

'''
  ############################# ^^^^^^^^^^^^^cleaning the txt not need for this task
'''

def condition(x):
    if x>0:
        return "Positive"
    elif x == 0:
        return "Neutral"
    else:
        return 'Negative'


tweets_df['sentiment'] = tweets_df['polarity'].apply(condition)

print(tweets_df.head())

sns.barplot(x='sentiment', y='polarity' , data=tweets_df)
#plt.savefig('sentiment.png')
plt.savefig('sentiment.png')
plt.show()






