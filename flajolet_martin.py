import os
from utils import pymmh3

INPUT_DIR = "data"
STREAM_FILENAME = "access_log_Jul95"


def compute_tail_len(val):
    bin_str = bin(val)[2:][::-1]
    # print val
    # print bin_str
    tail_len = bin_str.find("1")
    # print tail_len
    # A string of all zeros
    if tail_len == -1:
        return 32
    return tail_len


def flajolet_martin_algorithm(num_hashes=128, num_groups=8, filename=STREAM_FILENAME, debug=False):
    estimates = [0 for j in range(num_hashes)]

    f = open(os.path.join(os.path.curdir, INPUT_DIR, STREAM_FILENAME))
    line = f.readline()

    curr = 0

    while line != "alyssa.p":
        curr += 1
        line = line.split(" ")[0]
        # Print progress every 100 documents.
        if (curr % 100000) == 0:
            # print "Now computing ", curr, " of 1891714: ", line
            print "     (" + str(curr) + " / 1891714 )"


        # Compute the hashes for the line
        hashes = [pymmh3.hash(line, seed=i) for i in range(num_hashes)]

        # Update the estimates
        for i in range(num_hashes):
            tail_len = compute_tail_len(hashes[i])
            if tail_len > estimates[i]:
                estimates[i] = tail_len

        line = f.readline()

    f.close()
    if debug:
        print " estimates", estimates

    # Expand estimates
    estimates_exp = [2 ** i for i in estimates]
    if debug:
        print " estimates_exp", estimates_exp

    # Compute the group estimates
    group_estimates = [0.0 for j in range(num_groups)]
    for i in range(num_hashes):
        group_estimates[i % num_groups] += float(estimates_exp[i] / num_groups)

    if debug:
        print " group_estimates", group_estimates

    # Sort to find the median
    group_estimates.sort()
    if debug:
        print " group_estimates", group_estimates

    if num_groups % 2 == 0:
        return (group_estimates[(num_groups / 2) - 1] + group_estimates[(num_groups / 2)]) / 2
    else:
        return group_estimates[(num_groups - 1) / 2]


if __name__ == "__main__":
    print flajolet_martin_algorithm()
