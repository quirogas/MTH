# Homework 4

__author__ = "Santiago Quiroga"
__version__ = "2/Oct/2017"

"""
In this fist part I explore the easiest way of creating a method that returns a list with all possible combinations 
for different cardinalities, in order to find a pattern.
"""

def doubles(list_of_elements):
    coordinate_list = []
    answer_list = []

    for i in range(len(list_of_elements)):
        for j in range(i + 1, len(list_of_elements)):
            coordinate_list.append(list_of_elements[i])
            coordinate_list.append(list_of_elements[j])
            answer_list.append(coordinate_list)
            coordinate_list = []

    return answer_list


def triplets(list_of_elements):
    coordinate_list = []
    answer_list = []

    for i in range(len(list_of_elements)):
        for j in range(i + 1, len(list_of_elements)):
            for k in range(j + 1, len(list_of_elements)):
                coordinate_list.append(list_of_elements[i])
                coordinate_list.append(list_of_elements[j])
                coordinate_list.append(list_of_elements[k])
                answer_list.append(coordinate_list)
                coordinate_list = []

    return answer_list


def quads(list_of_elements):
    coordinate_list = []
    answer_list = []

    for i in range(len(list_of_elements)):
        for j in range(i + 1, len(list_of_elements)):
            for k in range(j + 1, len(list_of_elements)):
                for l in range(k + 1, len(list_of_elements)):
                    coordinate_list.append(list_of_elements[i])
                    coordinate_list.append(list_of_elements[j])
                    coordinate_list.append(list_of_elements[k])
                    coordinate_list.append(list_of_elements[l])

                    answer_list.append(coordinate_list)
                    coordinate_list = []

    return answer_list


def penta(list_of_elements):
    coordinate_list = []
    answer_list = []

    for i in range(len(list_of_elements)):
        for j in range(i + 1, len(list_of_elements)):
            for k in range(j + 1, len(list_of_elements)):
                for l in range(k + 1, len(list_of_elements)):
                    for m in range(l + 1, len(list_of_elements)):
                        coordinate_list.append(list_of_elements[i])
                        coordinate_list.append(list_of_elements[j])
                        coordinate_list.append(list_of_elements[k])
                        coordinate_list.append(list_of_elements[l])
                        coordinate_list.append(list_of_elements[m])

                        answer_list.append(coordinate_list)
                        coordinate_list = []

    return answer_list


####################################################################################################################
"""
After analysing the previous methods I developed a recursive method that is able to handle any type of cardinality
if the combination is possible.
"""

answer_list = []


# This method will return a list with all  the possible combinations of a given cardinality.
# (inception level refers to the number of nested for loops before the current
#  one where the first loop would have inception level 0 since there is 0 loops before it).
def masterlistgenerator(list_of_elements, cardinality, result=[], index=0, inception_lv=0):
    # This loop will iterate though the given list
    for i in range(index, len(list_of_elements)):
        # This statement will check if the cardinality og the given list is bigger than 1 in order to know the
        # inception lv of the loop. the idea is to get to cardinality 1 which means there is no more further
        # inceptions needed, so it would be time to perform the else logic.
        if cardinality > 1:
            # Increases the index in order to prevent using a repeated index
            index += 1

            # Appends the value of a given position for the given inception before entering the next inception.
            result.append(list_of_elements[i])

            # Creates a new inception in order to meet the cardinality requirements.
            masterlistgenerator(list_of_elements, cardinality - 1, result, index, inception_lv + 1)

            # Removes the number in the result list according to the inception lv in order to prevent repetition.
            result.pop(inception_lv)
        else:
            # Appends the last value to the list
            result.append(list_of_elements[i])

            # Appends the list of elements to the answer list
            answer_list.append(result[:])

            # Removes the last added digit in order to add new ones.
            result.pop()

    # Returns a list with all possible combinations of the given cardinality.
    return answer_list


# Tests for quality assurance ;)
print doubles(range(1, 6))
print masterlistgenerator(range(1, 6), 2)
answer_list = []
print triplets(range(1, 6))
print masterlistgenerator(range(1, 6), 3)
answer_list = []
print quads(range(1, 6))
print masterlistgenerator(range(1, 6), 4)
answer_list = []
print penta(range(1, 8))
print masterlistgenerator(range(1, 8), 5)
