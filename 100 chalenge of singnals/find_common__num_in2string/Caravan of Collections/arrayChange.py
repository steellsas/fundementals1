#
# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one.
# Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
#
# Example
#
# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.

def arrayChange(inputArray):
    move =0
    for i in range(len(inputArray)-1):
        move += 1
        for j in range(0,len(inputArray)-i-1):
            if inputArray[j] > inputArray[j + 1]:
                inputArray[j],inputArray[j+1] = inputArray[j+1],inputArray[j]
                move += 1

    return  move


def count_changes(lst):
    answer = 0
    for i in range(0,len(lst)-1):
         if not lst[i+1] > lst[i]:

             dif = abs(lst[i+1]-lst[i]) +1
             print(dif)
             answer+= dif
             lst[i+1]= lst[i+1]+dif

    return answer



ary =[-1000, 0, -2, 0]
print(count_changes(ary))