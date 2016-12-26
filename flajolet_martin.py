import os
from utils import lookup3

NUM_HASHES = 64
NUM_GROUPS = 8
INPUT_DIR = "data"
STREAM_FILENAME = "access_log_Jul95"


def compute_tail_len(val):
    bin_str = bin(val)[2:][::-1]
    tail_len = bin_str.find("1")

    # A string of all zeros
    if tail_len == -1:
        return 32

    return tail_len


def flajolet_martin_algorithm(filename=STREAM_FILENAME):
    estimates = [0 for j in range(NUM_HASHES)]

    f = open(os.path.join(os.path.curdir, INPUT_DIR, STREAM_FILENAME))
    line = f.readline()

    curr = 0

    while line != "alyssa.p":
        curr += 1
        print "Now computing ", curr, " of 1891714: ", line

        # Compute the hashes for the line
        hashes = [lookup3.hashlittle(line, initval=i) for i in range(NUM_HASHES)]

        # Update the estimates
        for i in range(NUM_HASHES):
            tail_len = compute_tail_len(hashes[i])
            if tail_len > estimates[i]:
                estimates[i] = tail_len

        line = f.readline()

    f.close()
    print estimates

    # Expand estimates
    estimates_exp = [2**i for i in estimates]
    print estimates_exp

    # Compute the group estimates
    group_estimates = [0.0 for j in range(NUM_GROUPS)]
    for i in range(NUM_HASHES):
        group_estimates[i % NUM_GROUPS] += float(estimates_exp[i] / NUM_GROUPS)

    print group_estimates

    # Sort to find the median
    group_estimates.sort()
    print group_estimates

    if NUM_GROUPS % 2 == 0:
        return (group_estimates[(NUM_GROUPS / 2) - 1] + group_estimates[(NUM_GROUPS / 2)]) / 2
    else:
        return group_estimates[(NUM_GROUPS - 1) / 2]

print flajolet_martin_algorithm()


