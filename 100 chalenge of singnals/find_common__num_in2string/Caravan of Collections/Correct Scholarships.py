# For the upcoming academic year the Coolcoders University should decide which students will get the scholarships.
# Scholarships are considered to be correctly distributed
# if all best students have it, but not all students in the university do.
# Obviously, only university students should be able to get a scholarship,
# i.e. there should be no outsiders in the list of the students that will get a scholarships.
#
# You are given lists of unique student ids bestStudents,
# scholarships and allStudents, representing ids of the best students,
# students that will get a scholarship and all the students in the university, respectively.
# Return true if the scholarships are correctly distributed and false otherwise

def correctScholarships(bestStudents, scholarships, allStudents):
    # all_best = True
    #
    # for x in bestStudents:
    #     if x not in scholarships:
    #         all_best = False
    #         break
    # is_student = True
    #
    # for y in scholarships:
    #     if y not in allStudents:
    #         is_student = False
    #         break
    # if all_best and is_student and len(allStudents) != len(scholarships):
    #     return True
    # else:
    #     return False

    return set(bestStudents) | set(scholarships) != set(allStudents) and not ((set(bestStudents) | set(scholarships)) - set(allStudents))

 # return len(scholarships) < len(allStudents) and sum([x in allStudents for x in scholarships]) == len(scholarships) \
 #        and sum([x in scholarships for x in bestStudents])==min(len(bestStudents), len(scholarships))

 #
 # return set(bestStudents) <= set(scholarships) < set(allStudents)

bestStudents = [3, 5]

scholarships = [3, 5, 7]
allStudents = [1, 2, 3, 4, 5, 6, 7]

print(correctScholarships(bestStudents, scholarships, allStudents))
bestStudents = [3, 5]
scholarships = [3, 5]
allStudents = [3, 5]
print(correctScholarships(bestStudents, scholarships, allStudents))
bestStudents = [3]
scholarships = [1, 3, 5]
allStudents = [1, 2, 3]
print(correctScholarships(bestStudents, scholarships, allStudents))