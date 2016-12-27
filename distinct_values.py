import os
from collections import defaultdict

INPUT_DIR = "data"
STREAM_FILENAME = "access_log_Jul95"


def distinct_values(filename=STREAM_FILENAME):
    values_dict = defaultdict(lambda: 0)

    f = open(os.path.join(os.path.curdir, INPUT_DIR, STREAM_FILENAME))
    line = f.readline()

    curr = 0

    while line != "alyssa.p":
        curr += 1
        line = line.split(" ")[0]
        print "Now computing ", curr, " of 1891714: ", line

        values_dict[line] += 1
        line = f.readline()

    return len(values_dict.keys())

if __name__ == "__main__":
    print distinct_values()