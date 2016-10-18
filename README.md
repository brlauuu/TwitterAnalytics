# TweetAnalytics

Simple script app for analysis of tweets using [Text Analytics API](https://www.microsoft.com/cognitive-services/en-us/text-analytics-api) and [Tweepy](http://www.tweepy.org). 

For now, the script analyses ~100 tweets that have the word 'Samsung' in them and returns the average sentiment value. 

## API keys

To running this script, first you have to acquire needed keys for accessing Text Analytics API and Twitter API. The process is easy and free. Here are the direct links :

- [Text Analytics API key](https://www.microsoft.com/cognitive-services/en-us/subscriptions)
- [Twitter API keys](https://apps.twitter.com)

Write your keys in the related files in the `.credentials` folder.


## Installation

Download this repository 

	git clone https://github.com/DjoleR/TwitterAnalytics.git

All the dependencies are in the `requirements.txt` file. To install them, simply run :

	pip install -r requirements.txt

To run the programm, type :

	python run-analytics.py [OPTION]

All options can be seen by running:
	
	python run-analytics.py --help

## Infos

The program currently runs with Python 2.*.

There's a few more things I plan to add, so stay tuned.
