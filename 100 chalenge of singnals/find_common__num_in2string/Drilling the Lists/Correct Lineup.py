"""
For the opening ceremony of the upcoming sports event an even number of athletes were picked.
They formed a correct lineup, i.e. such a lineup in which no two boys or two girls stand together.
 The first person in the lineup was a girl. As a part of the performance, adjacent pairs of athletes
 (i.e. the first one together with the second one, the third one together with the fourth one, etc.)
  had to swap positions with each other.

Given a list of athletes, return the list of athletes after the changes,
 i.e. after each adjacent pair of athletes is swapped.

 Example

For athletes = [1, 2, 3, 4, 5, 6], the output should be
correctLineup(athletes) = [2, 1, 4, 3, 6, 5].

Input/Output

"""
def correctLineup(athletes):
    return reduce(lambda x,y: x+y, zip(athletes[1::2], athletes[::2]))
#
# list(sum(zip(athletes[1::2], athletes[0::2]), ()))
        # [at
# hletes[i+(-1)**i] for i in range(len(athletes))]
# return [athletes[i+1] if i%2 == 0 else athletes[i-1] for i in range(0,len(athletes)) ]
# [el for tup in zip(athletes[1::2], athletes[::2]) for el in tup]

athletes = [1, 2, 3, 4, 5, 6]
print(correctLineup(athletes))
