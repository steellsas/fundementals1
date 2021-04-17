def commonCharacterCount(s1, s2):


    my_dic1 = {}
    for i in s1:
        if i in my_dic1.keys():
            my_dic1[i] += 1
        else:
            my_dic1[i] = 1
    my_dic2 = {}
    for j in s2:
        if j in my_dic2.keys():
            my_dic2[j] += 1
        else:
            my_dic2[j] = 1
    answer = 0
    for k in my_dic1.keys():
        if k in my_dic2.keys():

            if my_dic1[k] > my_dic2[k]:
                ch_common = my_dic1[k] - (my_dic1[k] - my_dic2[k])

            else:
                ch_common =my_dic2[k] - (my_dic2[k] - my_dic1[k])
            print(ch_common,)
            answer = answer + ch_common
    print(my_dic1,my_dic2)
    return answer

st1 = "zzzz"
st2 =  "zzzzzzz"
s1= "aabcc"
s2= "adcaa"

# print(commonCharacterCount(st1,st2))
print(commonCharacterCount(s1,s2))

