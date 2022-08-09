import json
import pandas as pd
from textblob import TextBlob


def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tweets_data = []
    for tweets in open(json_file,'r'):
        tweets_data.append(json.loads(tweets))
    
    
    return len(tweets_data), tweets_data

class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tweets_list):
        """
	Initialize the calss
	Args : list of the tweets
        """
        self.tweets_list = tweets_list

    # 

    def find_statuses_count(self)->list:
       	"""
       	statuses_count
       	Return: statuses_count
	"""
        statuses_count = [X['user']['statuses_count']  if 'user' in X else '' 
	for X in self.tweets_list]
        return statuses_count
        
    def find_full_text(self)->list:
        """
       	find_full_text 
       	Return: the tweets text 
	"""
        text = [X['full_text'] for X in self.tweets_list]
        return text
    
    def find_sentiments(self, text)->list:
        """
        find_sentiments
        Return: list of polarity and subjectivity
        """
        polarity = []
        subjectivity = []
        for tweet in text:
            blob = TextBlob(tweet)
            sentiment = blob.sentiment
            polarity.append(sentiment.polarity)
            subjectivity.append(sentiment.subjectivity)
        return polarity, subjectivity
    
    def find_created_time(self)->list:
        """
        The time of the tweets
        Return: list of created_at
        """
        created_at = [x['created_at'] for x in self.tweets_list]
        return created_at

    def find_source(self)->list:
        """
        Return: source
        """
        source = [x['source'] for x in self.tweets_list]
        return source

    def find_screen_name(self)->list:
        """
        Return: list of screen_name
        """
        screen_name = [X['user']['screen_name'] if 'user' in X else '' 
	for X in self.tweets_list]
        return screen_name
        
    def find_followers_count(self)->list:
        """
        Return: list of followers_count
        """
        followers_count = [X['user']['followers_count'] if 'user' in X else 0 
	for X in self.tweets_list]
        return followers_count
        
    def find_friends_count(self)->list:
        """
        Return: list of friends_count
        """
        friends_count = [X['user']['friends_count'] if 'user' in X else 0 
	for X in self.tweets_list]
        return friends_count
        
    def is_sensitive(self)->list:
        """
        Return: list of is_sensitive
        """
        is_sensitive = [X['possibly_sensitive'] if 'possibly_sensitive' 
	in X.keys() else '' for X in self.tweets_list]
        return is_sensitive

    def find_favourite_count(self)->list:
        """
        Return: list of favourite_count
        """
        favourite_count = [X['retweeted_status']['favorite_count'] 
	if 'retweeted_status' in X.keys() else 0 for X in self.tweets_list]
        return favourite_count
        
    def find_retweet_count(self)->list:
        """
        Return: list of retweet_count
        """
        retweet_count = [X['retweet_count'] if 'retweet_count' in X.keys() 
	else 0 for X in self.tweets_list]
        return retweet_count
        
    def find_hashtags(self)->list:
        """
        Return: list of hashtags
        """
        hashtags = [X['entities']['hashtags'] if 'entities' in X.keys() 
	else '' for X in self.tweets_list]
        return hashtags
        
    def find_mentions(self)->list:
        """
        Return: list of mentions
        """
        mentions = [X['entities']['user_mentions'] if 'entities' in X.keys() 
	else '' for X in self.tweets_list]
        return mentions

    def find_lang(self)->list:
        """
        Return: list of lang
        """
        lang = [X['lang'] for X in self.tweets_list]
        return lang
        
    def find_location(self)->list:
        """
        Return: list of Geo location
        """
        location = [X['user']['location'] if 'user' in X.keys() else '' 
	for X in self.tweets_list]
        
        return location

    
    def get_tweet_df(self, save=True) -> pd.DataFrame:
        """
        Return: the data file in csv format
        """

        columns = ['created_at', 'source', 'original_text', 'polarity', 
	'subjectivity', 'lang', 'favourite_count', 'retweet_count', 
	'original_author', 'followers_count', 'friends_count', 
	'possibly_sensitive', 'hashtags', 'user_mentions', 'place']

        created_at = self.find_created_time()
        source = self.find_source()
        text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(text)
        lang = self.find_lang()
        fav_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        screen_name = self.find_screen_name()
        follower_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        sensitivity = self.is_sensitive()
        hashtags = self.find_hashtags()
        mentions = self.find_mentions()
        location = self.find_location()

        data = zip(created_at, source, text, polarity, subjectivity,
        lang, fav_count, retweet_count, screen_name, follower_count,
        friends_count, sensitivity, hashtags, mentions, location)
        df = pd.DataFrame(data=data, columns=columns)    
        
        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')

        return df

                
if __name__ == "__main__":
    	# required column to be generated you should be creative and add 
	# more features
    	columns = ['created_at', 'source', 'original_text', 'clean_text', 
	'sentiment', 'polarity', 'subjectivity', 'lang', 'favorite_count', 
	'retweet_count', 'original_author', 'screen_count', 'followers_count', 
	'friends_count', 'possibly_sensitive', 'hashtags', 'user_mentions', 
	'place', 'place_coord_boundaries']
    	_, tweet_list = read_json("/home/ayman/Desktop/10Academy/Week-0/data/global_twitter_data.json")
    	tweet = TweetDfExtractor(tweet_list)
    	tweet_df = tweet.get_tweet_df() 

