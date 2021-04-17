def allLongestStrings(inputArray):
    lst_len = [len(x) for x in inputArray ]
    maxlen = max(lst_len)
    answer =[item for item in inputArray if len(item) == maxlen]

    return answer

input_array = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(input_array))