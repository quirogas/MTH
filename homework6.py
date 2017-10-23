# Homework 6
__author__ = "Santiago Quiroga"
__version__ = "23/Oct/2017"


# This function will return a list with the difference between each element .
def difference(sequence):
    # Local variable that keeps track of the final list.
    difference_list = []

    # This loop iterates though the sequence.
    for item in sequence:
        # Checks if the current item is the last item of the sequence.
        if sequence.index(item) != len(sequence) - 1:
            # Adds the difference between the two items into the difference_list.
            difference_list.append(sequence[sequence.index(item) + 1] - item)

    # Returns the difference list
    return difference_list


# This function returns a True if the sequence has a constant difference pastern after two iterations.
def isseconddegree(sequence):
    # Local variable that keeps track of the final list.
    second_degree = difference(difference(sequence))

    # This loop iterates though the sequence.
    for item in second_degree:
        # Checks if the current item is the last item of the sequence.
        if second_degree.index(item) != len(second_degree) - 1:
            # Checks if all the values are constant
            if second_degree[second_degree.index(item) + 1] != item:
                # Returns false when the list isn't constant
                return False

    # Returns true when the list is constant
    return True


# Tests for quality assurance ;)
print difference([2, 5, 3, 7, -1, 2])
print difference(range(0,10))
print isseconddegree([1, 6, 13, 22, 33, 46, 61, 78])
print isseconddegree([1, 2, 4, 8, 16, 32, 64])
