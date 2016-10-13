import tweepy

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

        self.api = tweepy.API(auth)

    def SearchTweets(self, query, language):
        public_tweets = []
        try:
            public_tweets = self.api.search(q=query, lang=language, count=100)
        except (tweepy.error.TweepError):
            print 'Please verify your Twitter API keys, it seems they\'re wrong.'
        return public_tweets
