# def my_function(year):
#     if year % 100 == 0:
#         answer = year // 100
#     else:
#         answer = year // 100 + 1
#     return answer
#
#
# a = my_function(1701)

#
#
# def checkPalindrome(inputString):
#     answer = False
#     if len(inputString) == 1:
#         answer = True
#
#     mid = len(inputString) // 2
#     print(inputString[0: mid], inputString[: mid-1:-1])
#     if len(inputString) % 2 == 0:
#         if inputString[0: mid] == inputString[: mid-1:-1]:
#             answer = True
#     else:
#         if inputString[0: mid+1] == inputString[: mid-1:-1]:
#             answer = True
#
#     return answer


# print(checkPalindrome('hlbeeykoqqqqokyeeblh'))
# print(checkPalindrome('aabaa'))

# def adjacentElementsProduct(inputArray):
#     firt_elem = inputArray[0]
#     second_elem = inputArray[1]
#     product = firt_elem * second_elem
#
#     for item in range(len(inputArray) - 1):
#         firt_elem = inputArray[item]
#         second_elem = inputArray[item + 1]
#         newproduct = firt_elem * second_elem
#         if newproduct > product:
#             product = newproduct
#     return product
# print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
#
# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
#
# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
#
#
#
# Example
#
# For n = 2, the output should be
# shapeArea(n) = 5;
# For n = 3, the output should be
# shapeArea(n) = 13.
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] integer n
#
# Guaranteed constraints:
# 1 ≤ n < 104.
#
# [output] integer
#
# The area of the n-interesting polygon.
#
# [Python 3] Syntax Tips


# # find poligon numer
# def shapeArea(n):
#     sum = 1
#     for item in range(1, n+1):
#         sum = sum + (item - 1) * 4
#         print(sum, item)
#     return sum
# print(shapeArea(1))
#
# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
# each statue having an non-negative integer size. Since he likes to make things perfect,
# he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1
# . He may need some additional statues to be able to accomplish that.
# Help him figure out the minimum number of additional statues needed.
# 430 / 5000
# Vertimo rezultatai
# Ratiorg gimtadienio proga iš „CodeMaster“ gavo įvairių dydžių

# def makeArrayConsecutive2(statues):
#     list_max = max(statues)
#     list_min = min(statues)
#
#     test = [x for x in range(list_min,list_max) if x not in statues]
#     return len(test)
#
# print(makeArrayConsecutive2([6, 2, 3, 8]))

def almostIncreasingSequence(sequence):
    i = 0
    not_d = True  # not deleted
    second_check = True
    while i < len(sequence)-1:
        if sequence[i] < sequence[i + 1]:
            increase = True
            i = i + 1
        else:
            if not_d:
                not_d = False
                new_list = sequence.copy()
                new_list.pop(i+1)
                sequence.pop(i)
                i = 0
                continue
            else:
                if second_check:
                    sequence =new_list.copy()
                    second_check =False
                    continue
                increase = False

                break

    if len(sequence) == 1:
        increase = True


    return  increase





test_lst = [3, 6, 5, 8, 10, 20, 15]
test2 =[3, 5, 67, 98, 3]
test7 = [10, 1, 2, 3, 4, 5]
print(almostIncreasingSequence(test2))