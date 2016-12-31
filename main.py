import os

import time

from alon_matias_szegedy import alon_matias_szegedy
from distinct_values import distinct_values
from flajolet_martin import flajolet_martin_algorithm
from second_moment import second_moment
from twitter_stream.stream import twitter_stream
from utils.print_statistic import print_statistic


TWITTER_DIR = "data/"
FILE_NAME_TWITTER = "twitter.txt"
FILE_NAME_STATISTIC = "stream_statistic.txt"


def compare_methos_ondataset(fm_num_hashes, fm_num_groups, ams_num_hashes):

    # parametri per FM sono: NUM_HASHES = 128, NUM_GROUPS = 8
    # parametri per AMS son:
    print ' Test with fm_num_hashes: {},  fm_num_groups: {}, ams_num_hashes: {}'.format(fm_num_hashes, fm_num_groups, ams_num_hashes)

    print '\n   Test flajolet_martin_algorithm: '
    F0_estimate = flajolet_martin_algorithm(fm_num_hashes,fm_num_groups)
    print '\n   Test distinct_values: '
    F0_real = distinct_values()

    print_statistic(1891714, F0_estimate, F0_real, fm_num_hashes, fm_num_groups)

    print '\n   Test alon_matias_szegedy:  '
    F2_estimate = alon_matias_szegedy(ams_num_hashes)
    print '\n   Test second_moment: '
    F2_real = second_moment()
    print_statistic(1891714, F2_estimate, F2_real, ams_num_hashes)

def compare_methos_twitter(number_test, fm_num_hashes, fm_num_groups, ams_num_hashes, frequency_statistic, number_of_tweets):

    twitter_stream(fm_num_hashes=fm_num_hashes, fm_num_groups=fm_num_groups, ams_num_hashes=ams_num_hashes, frequency_statistic=frequency_statistic,
                   number_of_tweets=number_of_tweets)

    # we have to change the name of the two files twitter and stream_statistic
    old_file = os.path.join(os.getcwd(), TWITTER_DIR, FILE_NAME_TWITTER)

    new_file = os.path.join(os.getcwd(),TWITTER_DIR, str(number_test) + FILE_NAME_TWITTER)
    os.rename(old_file, new_file)

    old_file = os.path.join(os.getcwd(), TWITTER_DIR, FILE_NAME_STATISTIC)
    new_file = os.path.join(os.getcwd(),TWITTER_DIR, str(number_test) + FILE_NAME_STATISTIC)
    os.rename(old_file, new_file)





if __name__ == "__main__":
    '''
    print "Test on data set: access_log_Jul95\n"
    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 1

    compare_methos_ondataset(fm_num_hashes=128, fm_num_groups=8, ams_num_hashes=64)

    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 2
    compare_methos()

    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 3
    compare_methos()

    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 4
    compare_methos()
    '''
    print "Test on Twitter"

    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 1
    compare_methos_twitter(1, fm_num_hashes=128, fm_num_groups=8, ams_num_hashes=64, frequency_statistic=1, number_of_tweets=10)

    # api error multiple connections not allowed
    time.sleep(20)
    print ' TEST..... ', 2
    compare_methos_twitter(2, fm_num_hashes=128, fm_num_groups=8, ams_num_hashes=64, frequency_statistic=1,
                           number_of_tweets=10)