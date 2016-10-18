import tweepy
import sys 
import jsonpickle
import os
import datetime

class TwitterApi:
    def __init__(self):
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""

        self.LoadCredentials()

    def LoadCredentials(self):
        # Read twitter credentials
        with open('.credentials/twitter-credentials') as tw_api_credentials:
            lines = tw_api_credentials.readlines();
            self.consumer_key = lines[0].split(':')[1].strip()
            self.consumer_secret = lines[1].split(':')[1].strip()
            self.access_token = lines[2].split(':')[1].strip()
            self.access_token_secret = lines[3].split(':')[1].strip()

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

        if (not self.api):
            print("Authentication failed")
            sys.exit(-1)

    def SearchTweets(self, query, language, count, storeFetchedTweets):
        public_tweets = []
        maxTweets = count 
        if count < 101:
            tweetsPerQuery = count
        else:
            tweetsPerQuery = 100

        fileName = 'tweets-' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))  + '.json' # We will store tweets in this file and retrieve all of them after we collect them all
        tweetCount = 0 # Number of tweets we retrieved
        max_id = -1L

        with open(fileName, 'w') as f:
            while tweetCount < maxTweets:
                new_tweets = []
                if maxTweets - tweetCount < 100:
                    tweetsPerQuery = maxTweets - tweetCount

                try:
                    new_tweets = self.api.search(q=query, lang=language, count=tweetsPerQuery)
                    if not new_tweets:
                        print("No more tweets found.")
                        break
                        
                    for tweet in new_tweets:
                        if storeFetchedTweets:
                            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                        
                        public_tweets.append(tweet)
               
                    tweetCount += len(new_tweets)
                    max_id = new_tweets[-1].id

                    print("Fetched " + str(len(public_tweets)) + " tweets in total.")
                    
                except (tweepy.error.TweepError):
                    if (len(public_tweets) > 0):
                        print("ERROR: Twitter API limit was reached.")
                    else:
                        print("Please verify your Twitter API keys, it seems they're wrong.")
                    
                    sys.exit(-1)

        return public_tweets
