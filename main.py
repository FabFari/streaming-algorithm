from alon_matias_szegedy import alon_matias_szegedy
from distinct_values import distinct_values
from flajolet_martin import flajolet_martin_algorithm
from second_moment import second_moment

''' INFO TO RETURN
   the number of records, the values of F0 (or F2) returned by your streaming algorithm,
   the true values F0 (or F2), the absolute and relative errors, the value of l, the group size (for FM)
'''

def print_statistic(n,F_estimate, F_real, ae, re, l, g=0):
    print "--------------------- STATISTICS -----------------------"
    if g != 0:  # for FM
        print "\n      number of records:  {}".format(n)
        print "     F0_estimate:  {}".format(F_estimate)
        print "     F0_real:  {}".format(F_real)
        print "     absolute errors: {}, relative errors: {}".format(ae, re)
        print "     value independent estimates: {}".format(l)
        print "     group size (FM): {}".format(g)
    else:
        print "\n       number of records:  {}".format(n)
        print "     F2_estimate:  {}".format(F_estimate)
        print "     F2_real:  {}".format(F_real)
        print "     absolute errors: {}, relative errors: {}".format(ae, re)
        print "     value independent estimates: {}".format(l)
    print "-------------------------------------------------------"

def compare_methos_ondataset(fm_num_hashes, fm_num_groups, ams_num_hashes):

    # parametri per FM sono: NUM_HASHES = 128, NUM_GROUPS = 8
    # parametri per AMS son:
    print ' Test with fm_num_hashes: {},  fm_num_groups: {}, ams_num_hashes: {}'.format(fm_num_hashes, fm_num_groups, ams_num_hashes)

    print '\n   Test flajolet_martin_algorithm: '
    F0_estimate = flajolet_martin_algorithm(fm_num_hashes,fm_num_groups)
    print '\n   Test distinct_values: '
    F0_real = distinct_values()

    print_statistic(1891714, F0_estimate, F0_real, 0,0, fm_num_hashes, fm_num_groups)

    print '\n   Test alon_matias_szegedy:  '
    F2_estimate = alon_matias_szegedy(ams_num_hashes)
    print '\n   Test second_moment: '
    F2_real = second_moment()
    print_statistic(1891714, F2_estimate, F2_real, 0, 0, ams_num_hashes)

def compare_methos_twitter(fm_num_hashes, fm_num_groups, ams_num_hashes):

    # parametri per FM sono: NUM_HASHES = 128, NUM_GROUPS = 8
    # parametri per AMS son:
    print ' Test with fm_num_hashes: {},  fm_num_groups: {}, ams_num_hashes: {}'.format(fm_num_hashes, fm_num_groups, ams_num_hashes)

    print '\n   Test flajolet_martin_algorithm: '
    F0_estimate = flajolet_martin_algorithm(fm_num_hashes,fm_num_groups)
    print '\n   Test distinct_values: '
    F0_real = distinct_values()

    print_statistic(1891714, F0_estimate, F0_real, 0,0, fm_num_hashes, fm_num_groups)

    print '\n   Test alon_matias_szegedy:  '
    F2_estimate = alon_matias_szegedy(ams_num_hashes)
    print '\n   Test second_moment: '
    F2_real = second_moment()
    print_statistic(1891714, F2_estimate, F2_real, 0, 0, ams_num_hashes)


if __name__ == "__main__":
    print "Test on data set: access_log_Jul95\n"
    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 1

    compare_methos_ondataset(fm_num_hashes=1, fm_num_groups=1, ams_num_hashes=2)
    '''
    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 2
    compare_methos()

    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 3
    compare_methos()

    print ' ##############################################################################################################################################################################'
    print ' TEST..... ', 4
    compare_methos()'''

    print "Test on Twitter"