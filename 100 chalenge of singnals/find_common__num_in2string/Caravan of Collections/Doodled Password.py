"""Your friend has been doodling during the lecture and wrote down several digits in a circle.
You're wondering if these digits might form the password to your friend's computer.
You're planning to prank him some time in the future, and hacking into his computer will definitely help. If the digits
written in the clockwise order indeed form a password, all you need to do is figure out which digit comes in it first.

Given a list of digits as they are written in the clockwise order, find all other combinations the password could possibly have."""

from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    # print(res)
    deque(map(lambda x: res[x].rotate(-x), range(n)), 0)
    # deque(map(lambda x: x[1].rotate(-x[0]), enumerate(res)), 0)
    return [list(d) for d in res]
digits = [1, 2, 3, 4, 5]
print(doodledPassword(digits))