# Import the necessary methods from "twitter" library
import io
import os
import unicodedata
from collections import defaultdict
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from alon_matias_szegedy import alon_matias_szegedy_real_time
from flajolet_martin import flajolet_martin_algorithm_real_time
from main import print_statistic


TWITTER_DIR = "data/"
FILE_NAME_TWITTER = "twitter.txt"
FILE_NAME_STATISTIC = "stream_statistic.txt"


def twitter_stream(fm_num_hashes, fm_num_groups, ams_num_hashes, frequency_statistic, debug=False):

    consumer_key = 'tZRi2DVFSeEl4K77R2yNLE8aQ'
    consumer_secret = 'Wnewl8PFjgBC9QlIimLpirYvdPvrvE9Mx4vEOeCvFPeuQr9s5G'
    access_token = '2341848095-rFwC9RZJceJGUvAsTEUivc8Hq6mdaHBGoFlNo44'
    access_secret = 'xFCaYxcGjN2X4aVCXu3cV0U8spIAiiVgwabygVfFkmIbU'
    oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

    # Initiate the connection to Twitter Streaming API
    tweets_stream = TwitterStream(auth=oauth)

    # Get stream iterator from two filters
    iterator = tweets_stream.statuses.filter(track="a", language="en", async=False)

    # Print each tweet in the stream to the screen
    # Here we set it to stop after getting 1000 tweets.
    # You don't have to set it to stop, but can continue running
    # the Twitter API to collect data for days or even longer.
    h_dict = defaultdict(lambda: 0)

    # initialize values
    estimates_fm = [0 for j in range(fm_num_hashes)]
    group_estimates_fm = [0.0 for j in range(fm_num_groups)]
    estimates_ams = [0 for j in range(ams_num_hashes)]
    tweet_count = 0
    avg = 0.0
    f = io.open(os.path.join(os.pardir, TWITTER_DIR, FILE_NAME_TWITTER), 'w', encoding='utf-8')
    for tweet in iterator:
        try:
            if len(tweet['entities']['hashtags']) != 0:
                if 'text' in tweet:  # only messages contains 'text' field is a tweet
                    for hashtag in tweet['entities']['hashtags']:
                        h = unicodedata.normalize('NFKD', hashtag['text']).encode('ASCII', 'ignore')
                        if len(h) != 0: # chinese caratects does not get convert
                            tweet_count += 1
                            f.write(tweet+'\n')

                            if debug:
                                print 'tweet_count: ', tweet_count
                            h_dict[str(h)] += 1
                            estimates_fm, group_estimates_fm, f0 = flajolet_martin_algorithm_real_time(h, estimates_fm, group_estimates_fm, fm_num_hashes, fm_num_groups, debug=False)
                            estimates_ams, avg = alon_matias_szegedy_real_time(h, estimates_ams, avg, ams_num_hashes, debug=False)
                        else:
                            if len(h) == 0:
                                if debug:
                                    print 'h: ', h
                                    print "hashtag['text']: ", hashtag['text']
                                break
                # each 100 hastag we show the statiscits
                if (tweet_count % frequency_statistic) == 0:

                    statistisc = print_statistic(tweet_count, f0, len(h_dict.keys()), estimates_fm, group_estimates_fm)
                    s = 0
                    for k in h_dict.keys():
                        s += h_dict[k]**2
                    # print_statistic(n, F_estimate, F_real, ae, re, l, g=0):
                    statistisc += print_statistic(tweet_count, avg, s, estimates_ams)


                    # close and open because the program continue to run, to stop it we have to kill the process,
                    # in this way we save the file session.
                    f.close()
                    f = io.open(os.path.join(os.pardir, TWITTER_DIR, FILE_NAME_TWITTER), 'w', encoding='utf-8')

                    # write json documents
                    with open("..\\{}\\{}".format(TWITTER_DIR, FILE_NAME_STATISTIC), "wt") as f:
                        f.write(statistisc)


        except Exception as e:
            print "errore",e
            continue

if __name__ == "__main__":
    print "twitter_stream: "
    twitter_stream(fm_num_hashes=128, fm_num_groups=8, ams_num_hashes=64, frequency_statistic=100)
