import pandas as pd
import string
import numpy as np
import re
from textblob import TextBlob



class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        return:
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']
        return df


    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        return:
        """
        self.df = df.drop_duplicates(subset='original_text')
        
        return self.df

    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        return:
        """    
        self.df['created_at'] = pd.to_datetime(df['created_at'], 
        errors='coerce')
        df = df[df['created_at'] >= '2020-12-31' ]
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count favorite_count 
	etc to numbers                
        return:
        """
        self.df['polarity'] = pd.to_numeric(df['polarity'], errors='coerce')
        self.df['retweet_count'] = pd.to_numeric(df['retweet_count'], 
	errors='coerce')
        self.df['favourite_count'] = pd.to_numeric(df['favourite_count'], 
	errors='coerce')
        self.df['subjectivity'] = pd.to_numeric(df['subjectivity'], 
	errors='coerce')
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        return:
        """
        self.df = df.query("lang == 'en' ")

        return df
        
        
        
        
if __name__ == "__main__":
    tweet_df = pd.read_csv("/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template/data/global_processed_tweet_data.csv")
    #tweet_df = pd.read_csv("/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template/data/africa_processed_tweet_data.csv")
    cleaner = Clean_Tweets(tweet_df)
    df = cleaner.drop_unwanted_column(cleaner.df)
    df = cleaner.drop_duplicate(df)
    df = cleaner.convert_to_numbers(df)
    df = cleaner.convert_to_datetime(df)
    df = cleaner.remove_non_english_tweets(df)
    
    df.to_csv('/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template/data/global_clean_tweet_data.csv', index=False)
    df.to_json('/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template/data/global_clean_tweet_data.json')
    
    #df.to_csv('/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template/data/africa_clean_tweet_data.csv', index=False)
    #df.to_json('/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template/data/africa_cleaned_tweet_data.json')
   
   
   
   
   
