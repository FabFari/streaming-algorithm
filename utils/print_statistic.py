''' INFO TO RETURN
   the number of records, the values of F0 (or F2) returned by your streaming algorithm,
   the true values F0 (or F2), the absolute and relative errors, the value of l, the group size (for FM)
'''
import math


def print_statistic(n, F_estimate, F_real, l, g=0):
    s = ''
    s += str("\n--------------------- STATISTICS -----------------------")

    ae = math.fabs(F_estimate-F_real)
    re = (ae/F_estimate)*100
    if g != 0:  # for FM
        s += str("\n")
        s += str("     number of records:  {} \n".format(n))
        s += str("     F0_real:      {}\n".format(F_real))
        s += str("     F0_estimate:  {}\n".format(F_estimate))
        s += str("     absolute errors: {}, relative errors: {}%\n".format(ae, re))
        s += str("     value independent estimates: {}\n".format(l))
        s += str("     group size (FM): {}\n".format(g))
    else:
        s += str("\n       number of records:  {}\n".format(n))
        s += str("     F2_real:      {}\n".format(F_real))
        s += str("     F2_estimate:  {}\n".format(F_estimate))
        s += str("     absolute errors: {}, relative errors: {}%\n".format(ae, re))
        s += str("     value independent estimates: {}\n".format(l))
    s += str("--------------------------------------------------------\n")

    print s
    return s

    # relativo = assoluto / reale
    # assolto = |stima - reale|
