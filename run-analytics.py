from twitter_api import *
from text_analytics_api import *

query = "Samsung"
language = "en"

print "Fetching tweets ..."
twApi = TwitterApi()
tweets = twApi.SearchTweets(query, language)

if len(tweets) is not 0:
    print "Tweets were sucessfully fetched"
    print "Generating sentiment ..."
    taApi = TextAnalyticsApi()
    tweetsSentiment = taApi.GetSentiment(tweets, language)

    avg_sent = 0
    total_tweets = 0
    if (tweetsSentiment != None):
        print "Sentiments were sucessfully generated"
        for ts in tweetsSentiment["documents"]:
            avg_sent += ts["score"]
            total_tweets += 1
            #print ts["id"] + ":" + str(ts["score"])

        print "Average sentiment for '" + query + "' on language '" + language + "' is : " + str(avg_sent/total_tweets)
        print "Total of " + str(total_tweets) + " tweets has been processed"
