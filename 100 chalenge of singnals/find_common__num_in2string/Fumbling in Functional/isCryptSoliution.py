# A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such
# that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.
#
# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits,
# solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], w
# hich should be interpreted as the word1 + word2 = word3 cryptarithm.
#
# If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping
# in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true.
# If it does not become a valid arithmetic solution, the answer is false.
#
# Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).
#
# Example
#
# For crypt = ["SEND", "MORE", "MONEY"] and
#
# solution = [['O', '0'],
#             ['M', '1'],
#             ['Y', '2'],
#             ['E', '5'],
#             ['N', '6'],
#             ['D', '7'],
#             ['R', '8'],
#             ['S', '9']]
# the output should be
# isCryptSolution(crypt, solution) = true.
#
# When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.
#
# For crypt = ["TEN", "TWO", "ONE"] and
#
# solution = [['O', '1'],
#             ['T', '0'],
#             ['W', '9'],
#             ['E', '5'],
#             ['N', '4']]
# the output should be
# isCryptSolution(crypt, solution) = false.
#
# Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.
crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

def isCryptSolution(crypt, solution):

    # test = list(map(crypt, l))
    ch_dir = { item[0]: int(item[1]) for item in solution}

    word1 = crypt[0]
    word2 = crypt[1]
    word3 = crypt[2]



    # word_in_number =''.join(str(ch_dir[ch])for ch in word1)

    # checking first word letter has zero
    word_start_zero = False
    if ch_dir[word1[0]] == 0 or ch_dir[word2[0]] == 0 or ch_dir[word3[0]] == 0:
        word_start_zero = True

    # word to digits
    numbers= [''.join(str(ch_dir[ch])for ch in word1) for word1 in crypt ]

    if (int(numbers[0]) + int(numbers[1])) == int(numbers[2]):
        if word_start_zero and int(numbers[2]) == 0 and len(numbers[2]) == len(str(int(numbers[2]))):
            return True
        elif word_start_zero:
            return False
        else :
            return True
    else:
        return False

print(isCryptSolution(crypt, solution))

# def find_value(solut, ch):
#     for item in solut:
#         if item[0] == ch:
#             return item[1]
# print(find_value(solution,'S'))

def isCryptSolution(crypt, solution):
    dic = {ord(c): d for c, d in solution}
    *v, = map(lambda x: x.translate(dic), crypt)
    return not any(x != "0" and x.startswith("0") for x in v) and \
        int(v[0]) + int(v[1]) == int(v[2])


def isCryptSolution(crypt, solution):
    crypt_s = crypt
    for i in range(0, 3):
        for s in solution:
            crypt_s[i] = crypt_s[i].replace(s[0], s[1])

        if crypt_s[i] != '0' and crypt_s[i][0] == '0':
            return False

    if int(crypt_s[0]) + int(crypt_s[1]) != int(crypt_s[2]):
        return False

    return True

