"""No time to explain! The World Government made contact with intelligent alien life,
 and needs you to send a message to the outer space.
 The aliens only receive messages that are stored in a sequence of lists of sizes 0, 1, 1, 2, 3, 5, ...,
  in other words those whose length increase according to the Fibonacci sequence.

The Government is too busy composing the message,
 and needs you to prepare the list in which the message should be sent.
  Given an integer n, return a list of n lists,
  where the first element consists is empty (consists of 0 zeros), the second element consists of 1 zero, and so on.

Example

For n = 6, the output should be

fibonacciList(n) = [[],
                    [0],
                    [0],
                    [0, 0],
                    [0, 0, 0],
                    [0, 0, 0, 0, 0]]"""

from functools import reduce
n = 6
def fibonacciList(n):
    return [[0] * x for x in reduce(lambda a,n: a + [a[-1]+a[-2]], range(0,n-2),[0, 1])]

print(fibonacciList(n))