""":cvarYou've come up with a really cool name for your future startup company,
 and already have an idea about its logo. This logo will represent a circle,
  with the prefix of a cyclic string formed by the company name written around it.

The length n of the prefix you need to take depends on the size of the logo.
You haven't yet decided on it, so you'd like to try out various options.
 Given the name of your company, return the prefix of the corresponding cyclic string containing n characters.

Example

For name = "nicecoder" and n = 15, the output should be
cyclicName(name, n) = "nicecoderniceco"."""

from itertools import cycle

def cyclicName(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)

name = "nicecoder"
n = 15
print(cyclicName(name, n))