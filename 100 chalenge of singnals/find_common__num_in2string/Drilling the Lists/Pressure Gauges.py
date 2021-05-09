"""
Harry dropped out of school to pursue his dreams and work in Pipes Corporations.
He is now in charge of a lot of pipes, and his task is to check the gauges twice a day.
 By analyzing the morning and evening pressures of each pipe, Harry should write a report about the minimum
 and the maximum pressure during the day.

Given the pressures Harry wrote down for each pipe,
 return two lists: the first one containing the minimum,
 and the second one containing the maximum pressure of each pipe during the day.

Example

For morning = [3, 5, 2, 6] and evening = [1, 6, 6, 6],
the output should be
pressureGauges(morning, evening) = [[1, 5, 2, 6], [3, 6, 6, 6]].

"""
from functools import reduce

def pressureGauges(morning, evening):
    return [list(map(lambda a,b: a if (a < b) else b,morning, evening)),list(map(lambda a,b: a if (a > b) else b,morning, evening))]
#  soliution
#   return zip(*map(sorted, zip(morning, evening)))
# return [[min(a, b) for a, b in zip(morning,evening)], [max(a, b) for a, b in zip(morning,evening)] ]
#  return list(zip(*[(min( t), max( t)) for t in zip(morning, evening)]))
#  return [list(map(min, zip(morning, evening))),
#            list(map(max, zip(morning, evening)))]
morning = [3, 5, 2, 6]
evening = [1, 6, 6, 6]

print(pressureGauges(morning, evening))