from twitter_api import *
from text_analytics_api import *
import sys
import datetime

def printHelp():
    print("\nUsage: python run-analytics.py [OPTION] [OPTION] ..")
    print("[OPTION]:")
    print("\t--language=<LN>\twhere <LN> takes value of two letter code for certain language (e.g. en, es, fr or pt - the languages that are supported by Text Analytics API). Default lang is English (en).")
    print("\t--query=<QUERY>\twhere <QUERY> takes value of query you want to search on Twitter (e.g. Twitter). This value has to be passed.\n")
    print("\t--count=<COUNT>\twhere <COUNT> takes value of number of tweets you want to analyse. Default value is set to 100.\n")
    print("\t--storeTweets=<OP>\twhere <OP> takes value of 'on' or 'off'. Default value is set to 'off'.\n")

query = ""
language = "en"
availableLanguages = ["en", "es", "fr", "pt"]
count = 100
storeFetchedTweets = False

for arg in sys.argv:
    if (arg == __file__):
        continue

    elif arg.startswith("--query="):
        query = arg.split('=')[1]

    elif arg.startswith("--language="):
        language = arg.split('=')[1]
        if language not in availableLanguages:
            print("Supplied language not supported. Pass in one of: en, es, fr, pt.")
            sys.exit(-1)

    elif arg.startswith("--count="):
        try:
            count = int(arg.split('=')[1])
        except:
            print("Invalid number passsed as count value: " + arg[arg.index('=') + 1:])
            sys.exit(-1)

    elif arg == ("--help"):
        printHelp()
        sys.exit(0)

    elif arg.startswith("--storeTweets="):
        if arg.split('=')[1] == "on":
            storeFetchedTweets = True
        elif arg.split('=')[1] == "off":
            storeFetchedTweets = False
        else:
            print("Invalid argument passed as storeTweets value: " + arg[arg.index('=') + 1:])
    else:
        print("Unknown option: " + arg + " Run python run-analytics.py --help for details.")
        sys.exit(-1)

if (query == ""):
    print("ERROR: Invalid parameter passed. Query cannot be an empty string.")
    sys.exit(-1)

print("Fetching tweets ...")
twApi = TwitterApi()
tweets = twApi.SearchTweets(query, language, count, storeFetchedTweets)

if len(tweets) is not 0:
    print("Tweets were sucessfully fetched")
    if storeFetchedTweets:
        print("Tweets are stored at: tweet-" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    print("Generating sentiment ...")
    taApi = TextAnalyticsApi()
    tweetsSentiment = taApi.GetSentiment(tweets, language)

    avg_sent = 0
    total_tweets = 0
    if (tweetsSentiment != None):
        print("Sentiments were sucessfully generated")
        for ts in tweetsSentiment["documents"]:
            avg_sent += ts["score"]
            total_tweets += 1
            #print(ts["id"] + ":" + str(ts["score"])

        if total_tweets > 0:
            print("Average sentiment for '" + query + "' on language '" + language + "' is : " + str(avg_sent/total_tweets))
            print("Total of " + str(total_tweets) + " tweets has been processed")
        else:
            print("ERROR: ")

