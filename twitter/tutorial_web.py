import tweepy
import unicodedata
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener, json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

consumer_key = 'tZRi2DVFSeEl4K77R2yNLE8aQ'
consumer_secret = 'Wnewl8PFjgBC9QlIimLpirYvdPvrvE9Mx4vEOeCvFPeuQr9s5G'
access_token = '2341848095-rFwC9RZJceJGUvAsTEUivc8Hq6mdaHBGoFlNo44'
access_secret = 'xFCaYxcGjN2X4aVCXu3cV0U8spIAiiVgwabygVfFkmIbU'


oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
# iterator = twitter_stream.statuses.sample()

iterator = twitter_stream.statuses.filter(track="a", language="en")

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 1000
tag = []
for tweet in iterator:

    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    try:
        if len(tweet['entities']['hashtags']) != 0:
            tweet_count -= 1
            # print json.dumps(tweet)

            if 'text' in tweet:  # only messages contains 'text' field is a tweet

                # print tweet['id']  # This is the tweet's id
                # print tweet['created_at']  # when the tweet posted
                # print "text: {}".format(unicodedata.normalize('NFKD', tweet['text']).encode('ASCII', 'ignore'))  # content of the tweet

                # print tweet['user']['id']  # id of the user who posted the tweet
                # print tweet['user']['name']  # name of the user, e.g. "Wei Xu"
                # print tweet['user']['screen_name']  # name of the user account, e.g. "cocoweixu"

                hashtags = []
                for hashtag in tweet['entities']['hashtags']:
                    hashtags.append(hashtag['text'])
                    tag.append(hashtag['text'])
                print hashtags


            # The command below will do pretty printing for JSON data, try it out
            # print json.dumps(tweet, indent=4)
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue

    if tweet_count <= 0:
        break


print "len beofore set: {}".format(len(tag))

print "len after set: {}".format(len(set(tag)))
print set(tag)