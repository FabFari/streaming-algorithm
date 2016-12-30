# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

from flajolet_martin import flajolet_martin_algorithm_real_time


def twitter_stream(tweet_count, fm_num_hashes, fm_num_groups, ams_num_hashes):
    consumer_key = 'tZRi2DVFSeEl4K77R2yNLE8aQ'
    consumer_secret = 'Wnewl8PFjgBC9QlIimLpirYvdPvrvE9Mx4vEOeCvFPeuQr9s5G'
    access_token = '2341848095-rFwC9RZJceJGUvAsTEUivc8Hq6mdaHBGoFlNo44'
    access_secret = 'xFCaYxcGjN2X4aVCXu3cV0U8spIAiiVgwabygVfFkmIbU'
    oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

    # Initiate the connection to Twitter Streaming API
    twitter_stream = TwitterStream(auth=oauth)

    # Get stream iterator from two filters
    iterator = twitter_stream.statuses.filter(track="a", language="en")

    # Print each tweet in the stream to the screen
    # Here we set it to stop after getting 1000 tweets.
    # You don't have to set it to stop, but can continue running
    # the Twitter API to collect data for days or even longer.
    tag = []

    estimates = [0 for j in range(fm_num_hashes)]
    # Compute the group estimates
    group_estimates = [0.0 for j in range(fm_num_groups)]

    for tweet in iterator:
        try:
            if len(tweet['entities']['hashtags']) != 0:
                tweet_count -= 1
                # print tweet
                if 'text' in tweet:  # only messages contains 'text' field is a tweet
                    hashtags = []
                    for hashtag in tweet['entities']['hashtags']:
                        hashtags.append(hashtag['text'])
                        tag.append(hashtag['text'])
                        print hashtag['text']
                        flajolet_martin_algorithm_real_time(hashtag['text'], estimates, group_estimates, fm_num_hashes, fm_num_groups, debug=True)
                        print 'after fm'


                    print 'hashtags: ',hashtags

        except:
            # read in a line is not in JSON format (sometimes error occured)
            continue

        if tweet_count <= 0:
            break

if __name__ == "__main__":
    print "twitter_stream: "
    twitter_stream(tweet_count=1, fm_num_hashes=128, fm_num_groups=8, ams_num_hashes=64)
