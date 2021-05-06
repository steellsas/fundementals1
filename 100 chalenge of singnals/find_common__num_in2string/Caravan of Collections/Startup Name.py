# You decided to found your own startup company and now want to choose a proper name for it.
#     There are three large companies that you want to compete against, and
#     since their names are quite popular you want to use their names as a starting point.
#     You want to use only popular characters in the name of your company, but not too mainstream.
#     You consider a character to be popular if it appears in at least two company names, and consider
#     it to be mainstream if it appears in all three.
#
# Given the names of the companies, return the list of characters that are popular but not mainstream sorted by their ASCII codes.



def startupName(companies):
    cmp1 = set(companies[0])

    cmp2 = set(companies[1])

    cmp3 = set(companies[2])


    # print(cmp2 - cmp1 | cmp1 - cmp2)
    # print(cmp3 - cmp2 | cmp2 - cmp3)
    # print(cmp3 - cmp1 | cmp3 - cmp1)


    # res = set(companies[0] + companies[1] + companies[2]) ^ (cmp1 ^ cmp2 ^ cmp3)
    res = ((comp1 | comp2 | comp3) - (comp1 ^ comp2 ^ comp3))
    return sorted(list(res))


companies = ["coolcompany", "nicecompany", "legendarycompany"]
print(startupName(companies))