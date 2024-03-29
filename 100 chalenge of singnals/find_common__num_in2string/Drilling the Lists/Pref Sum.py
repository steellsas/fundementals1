"""There is a great technique that allows finding sums of consecutive elements in the given array extremely fast.
 It is based on the usage of prefix sums. Given array a, your task is to calculate all its prefix sums.

Example

For a = [1, 2, 3], the output should be
prefSum(a) = [1, 3, 6].

Here's how the prefix sums can be calculated: [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6].

"""
from numpy import cumsum

a = [1, 2, 3]

def prefSum(a):
    return comsum(a)


    # list(map(lambda x: , [a[:i]  for i in range(len(a))]))

# from itertools import accumulate
#
# def prefSum(a):
#     return list(accumulate(a))
return list(functools.reduce(lambda x, y: x + [x[-1]+ y], a[1:], [a[0]]))


print(prefSum(a))