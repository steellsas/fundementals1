def getPoints(answers, p):
    questionPoints = lambda i,ans: i+1 if ans =='true' else -1* p

    res = 0
    for i, ans in enumerate(answers):
        res+=questionPoints(i, ans)

    return res


a = ['true','true','false','true']
p =2
# print(getPoints(a, p))++

"""You are given a list of students who want to apply to the internship at CodeSignal. 
For the ith student you know their full name students[i], which can consist of up to 5 
words (where a word is a set of consecutive letters). It is guaranteed that the surname 
is always the last name of student's full name.

Your task is to sort the students lexicographically by their surnames. 
If two students happen to have the same surname, 
their order in the result should be the same as in the original list."""
# def sortStudents(students):
#     students.sort(key=lambda students: students.split(" ")[-1], reverse=False)
#
#     return students
#
# students = ["John Smith", "Jacky Mon Simonoff",
#             "Lucy Smith", "Angela Zimonova"]
#
# print(sortStudents(students))

# You've been preparing all night for the upcoming test and entered the class certain that you will ace it.' \
#    ' Now that you received the test questions, you died inside a little:' \
#    ' looks like you prepared for the test on a completely different topic.
#
# You're not even sure if you should bother to answer the questions.' \
#    ' You still have some hope though: it is known that there's
# a glitch in the test preparing system, so that if the sum of digits of question ids is divisible by
# k, the answer to each question has a 90% probability to be an A.
#
# Given the list of question ids, determine if the sum of their digits is divisible by k to see if it's worth trying to pass the test.
#
# def isTestSolvable(ids, k):
#     digitSum = lambda questionId: sum(int(str(questionId).split()))
#
#     sm = 0
#     for questionId in ids:
#         sm += digitSum(questionId)
#     return sm % k == 0
#
# ids = [529665, 909767, 644200]
#
# test = sum([int(x) for x in str(ids[0])])

def createSpiralMatrix(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    res =  [[i,j] for i in range(n)  for j in range(n)]

    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 <= nextPos[0] < n and
                0 <= nextPos[1] < n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res

print(createSpiralMatrix(3))
# resul =  [(i ,j) for i in range(3)  for j in range(3)]
# print(resul)