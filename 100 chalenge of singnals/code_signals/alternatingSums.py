

# def alternatingSums(a):
#     sum1 = 0
#     sum2 = 0
#     for i in range(len(a)):
#         index = i+1
#         if index % 2 == 0:
#             sum2 = sum2 + a[i]
#         else:
#             sum1 = sum1 + a[i]
#     return (sum1, sum2)
#
# # a = [50, 60, 60, 45, 70]
# # a =[100,50]
# a = [50, 60, 60, 45, 70]
# print(alternatingSums(a))

# Given a rectangular matrix of characters, add a border of asterisks(*) to it.


# def addBorder(picture):
#
#     line = '*'* (len(picture[0]) + 2 )
#     answer = [line]
#     for item in picture:
#         inline = '*' + item + '*'
#         answer.append(inline)
#     answer.append(line)
#
#     return answer
#
#
# picture = ["abc",
#            "ded"]
#
# print(addBorder(picture))

# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
#
# Given two arrays a and b, check whether they are similar.

def areSimilar(a, b):
    same = True
    one = True
    go  =True
    i = 0
    j = 0
    while go:

        if a[i] == b[j]:
            same = True
        else:
            if one:
               b[j] ,b[j+1] = b[j+1], b[j]
               one = False
               continue

            same = False
        j = j + 1
        i= i + 1
        if j == len(b):
            go = False
    if same:
        return True
    else:
        return False
a = [1, 2, 3]
b = [2, 1, 2]

print(areSimilar(a, b))


