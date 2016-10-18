from twitter_api import *
from text_analytics_api import *
import sys

def printHelp():
    print("\nUsage: python run-analytics.py [OPTION] [OPTION] ..")
    print("[OPTION]:")
    print("\t--language=<LN>\twhere <LN> takes value of two letter code for certain language (e.g. en, ru etc). Default lang is English (en).")
    print("\t--query=<QUERY>\twhere <QUERY> takes value of query you want to search on Twitter (e.g. Twitter). This value has to be passed.\n")

query = ""
language = ""

for arg in sys.argv:
    if (arg == __file__):
        continue
    elif arg.startswith("--query"):
        query = arg.split('=')[1]
    elif arg.startswith("--language"):
        language = arg.split('=')[1]
    elif arg == ("--help"):
        printHelp()
        sys.exit()
    else:
        print("Unknown option. Run python run-analytics.py --help for details.")
        sys.exit()

if (query == ""):
    print("ERROR: Invalid parameter passed. Query cannot be an empty string.")
    sys.exit()

if (language == ""):
    print("WARNING: No language is selected, default lang is set.")
    language = "en"

print("Fetching tweets ...")
twApi = TwitterApi()
tweets = twApi.SearchTweets(query, language)

if len(tweets) is not 0:
    print("Tweets were sucessfully fetched")
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

        print("Average sentiment for '" + query + "' on language '" + language + "' is : " + str(avg_sent/total_tweets))
        print("Total of " + str(total_tweets) + " tweets has been processed")
