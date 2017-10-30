# Homework 7
__author__ = "Santiago Quiroga"
__version__ = "30/Oct/2017"


# Recursive function: F(a_n)= CONSTANT_ONE * a_(n-1) + CONSTANT_TWO * a_(n-2)
def recursivefunction(constant_one, constant_two, a_zero, a_one, iterations=15):
    # Local variable that keep track of the final list
    final_list = [a_zero, a_one]

    # This loop does (iterations - 2) iteration. If no input given to iterations then th default is 15
    for n in range(2, iterations):
        final_list.append(((constant_one * final_list[n - 1]) + (constant_two * final_list[n - 2])))

    # Return a list with iterations number of results.
    return final_list


# Test fot quality assurance ;)
print recursivefunction(1, 2, 3, 4)
print recursivefunction(5, 6, 7, 8)
print recursivefunction(4, 3, 2, 1)
print recursivefunction(1, 3, 2, 4)
