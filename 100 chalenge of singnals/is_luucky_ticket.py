# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky
# if the sum of the first half of the digits is equal to the sum of the second half.
#
# Given a ticket number n, determine if it's lucky or not.
def isLucky(n):
    n_str = str(n)
    mid = len(n_str) // 2
    lst=[int(x) for x in n_str[:mid]]
    lst2 = [int(x) for x in n_str[mid:]]
    if sum(lst) == sum(lst2):
        return True
    else:
        return False
# ---------------------------------------------------
# Some people are standing in a row in a park.
# There are trees between them which cannot be moved.
# Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
# People can be very tall!

def sortByHeight(a):
    # from list deleting  -1  and take index
    neg_index = []
    for i in range(len(a)):
        if a[i] == -1:
            neg_index.append(i)
    lst = [x for x in a if x != -1]
    answer = sorted(lst)
    for i in neg_index:
        answer.insert(i,-1)
    return answer

aa = [-1, 150, 190, 170, -1, -1, 160, 180]
sortByHeight(aa)

#
def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
            print (s[:start])
        if s[i] == ")":
            end = i
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s
s ="(bar)"
print(reverseParentheses(s))