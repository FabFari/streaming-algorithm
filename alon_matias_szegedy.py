import os
from utils import pymmh3

NUM_HASHES = 64
INPUT_DIR = "data"
STREAM_FILENAME = "access_log_Jul95"


def alon_matias_szegedy(num_hashes=64, filename=STREAM_FILENAME, debug=False):
    estimates = [0 for j in range(num_hashes)]

    f = open(os.path.join(os.path.curdir, INPUT_DIR, STREAM_FILENAME))
    line = f.readline()

    curr = 0

    while line != "alyssa.p":
        curr += 1
        line = line.split(" ")[0]
        if (curr % 100000) == 0:
            # print "Now computing ", curr, " of 1891714: ", line
            print "     (" + str(curr) + " / 1891714 )"

        for i in range(num_hashes):
            estimates[i] += 1 if pymmh3.hash(line, seed=i) % 2 == 0 else -1

        line = f.readline()
    if debug:
        print estimates

    estimates = [e ** 2 for e in estimates]
    if debug:
        print estimates

    sum_est = 0

    for e in estimates:
        sum_est += e

    return float(sum_est) / float(num_hashes)

if __name__ == "__main__":
    print alon_matias_szegedy()
