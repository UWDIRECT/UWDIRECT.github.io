from statistics import mean
import numpy.random as nprnd
from statistics import stdev
# main function of file, I think
def MyFuNcTiOn(ARGUMENT):
    m = mean(ARGUMENT)
    s = stdev(ARGUMENT)
    gt3sd = 0
    lt3sd = 0
    for m in ARGUMENT:
        if m > m + (s * 2):
            gt3sd += 1
        elif m < m - (s * 2):
            lt3sd += 1
    return(gt3sd, lt3sd)
def AnotherFunction(anumber = 1000, anothernumber = 1000):
    l = nprnd.randint(anothernumber, size = anumber)
    return(MyFuNcTiOn(l))
a,b=AnotherFunction(anumber = 1000, anothernumber = 1000)
print('found %d random values greather than 2 * sd and %d less than 2 * sd' % (a, b))
