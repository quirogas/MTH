from operator import index

# Homework 2
__author__ = "Santiago Quiroga"
__version__ = "10/Sep/2017"


def intersect(list_a, list_b):
    # Local variable
    intersection = []
    # iterates though the elements in list_a
    for elements_a in list_a:
        # iterates though the elements in list_b
        for elements_b in list_b:
            # if an element appears in both list, then is added to a the intersection list
            if elements_a == elements_b:
                intersection.append(elements_a)
    return intersection


def union(list_a, list_b):
    # Local variables
    combined_list = list_a + list_b
    intersection_list = intersect(list_a, list_b)

    # Iterates through the element in the combined_list
    for elements_u in combined_list:
        # Iterates through thr elements in the intersection_list
        for elements_i in intersection_list:
            # Removes all the elements that are repeated from the list   
            if elements_i == elements_u:
                combined_list.remove(index(elements_u))
                intersection_list.remove(index(elements_i))

    # Organises the list in ascending order
    combined_list.sort()

    return combined_list


def inverseimage(function, range_item):
    # Local variables
    inverse_image = []

    # Iterates through the domain of the function
    for domain in function.keys():
        # If the domain has the indicated range is added to the inverse_image list
        if function[domain] == range_item:
            inverse_image.append(domain)

    return inverse_image


# Tests for quality assurance ;)
test_set = {'a': 0, 'b': 1, 'c': 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0, 9: 0, 10: 0}
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [1, 3, 5, 7, 9, 11, 13, 15, 17]

print inverseimage(test_set, 1)
print (intersect(list_a, list_b))
print (union(list_a, list_b))
