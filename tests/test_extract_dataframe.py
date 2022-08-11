import unittest
import pandas as pd
import sys, os

import json

sys.path.append(os.path.abspath(os.path.join("/home/ayman/Desktop/10Academy/Week-0-assignment/bugfix/Twitter_Data_Analysis_Template/")))
from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below
sampletweetsjsonfile = "/home/ayman/Desktop/10Academy/Week-0/data/global_twitter_data.json"   #put here the path to where you placed the file e.g. ./sampletweets.json. 
_, tweet_list = read_json(sampletweetsjsonfile)

columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place",
    "place_coord_boundaries",
]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file
		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()
        
    def test_find_statuses_count(self):
        statuses_count = [8097,5831,1627,1627,18958]
        self.assertEqual(
        self.df.find_statuses_count(), statuses_count)

    def test_find_sentiments(self):
        subjectivity = [0.190625 , 0.1 , 0.0 , 0.35 , 0.55625 ]
        polarity = [-0.125 , -0.1 , 0.0 , 0.1 , -6.93889390390722E-18 ] 
        self.assertAlmostEqual(self.df.find_sentiments(self.df.find_full_text()), (polarity,subjectivity),places=8 )  
        
    def test_find_followers_count(self):
        followers_count = [20497 , 65 , 85 , 85 , 910 ] #<provide a list of the first five follower counts>
        self.assertEqual(self.df.find_followers_count(), followers_count)
        
    def test_find_screen_name(self):
        name = ['i_ameztoy' , 'ZIisq' , 'Fin21Free' , 'Fin21Free' , 'VizziniDolores']
        self.assertEqual(self.df.find_screen_name(), name)
    def test_find_followers_count(self):
        followers_count = [20497 , 65 , 85 , 85 , 910 ] #<provide a list of the first five follower counts>
        self.assertEqual(self.df.find_followers_count(), followers_count)
        
    def test_find_friends_count(self):
        friends_count = [2621 , 272 , 392 , 392 , 2608] # <provide a list of the first five friend's counts>
        self.assertEqual(self.df.find_friends_count(), friends_count)
        
    def test_find_is_sensitive(self):
        sensitive = ['' , '' , '' , '' , '' ]
        self.assertEqual(self.df.is_sensitive(), sensitive)
        
        
    def test_find_full_text(self):
        text = ['rt extra random image i lets focus in one very specific zone of the western coast gt longjing district taichung','rt media explains the military reasons for each area of the drills in the strait read the labels in the pi','china even cut off communication they dont anwer phonecalls from the us but here clown enters the stage to ask to change putins mind','putin to i told you my friend taiwan will be a vassal state including nukes much like the ukrainian model i warned you but it took pelosi to open chinas eyes','rt i m sorry i thought taiwan was an independent country because it had its own government currency military travel d']

        self.assertEqual(self.df.find_full_text(), text)

if __name__ == "__main__":
    	unittest.main()
        #unittest.test_find_statuses_count()
