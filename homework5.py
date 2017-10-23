# Homework 5
__author__ = "Santiago Quiroga"
__version__ = "6/Oct/2017"


# This function will return a list with the number of trees per backyard.
def binarytoanalogy(list):
    # local variables for value tracking.
    answer_list = []
    counter = 0

    # Iterates though the list.
    for i in list:

        # Check for trees or fences.
        if i == 1:
            # Adds the number of threes in the current backyard and resets the counter.
            answer_list.append(counter)
            counter = 0
        else:
            # counts the number of tress in a backyard.
            counter += 1

    # Add the values of the last backyard.
    answer_list.append(counter)

    # Returns a list with all the number of trees in each backyard.
    return answer_list


# Tests for quality assurance ;)
print binarytoanalogy([0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1])
print binarytoanalogy([0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0])
print binarytoanalogy([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print binarytoanalogy([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])