# Homework 3
__author__ = "Santiago Quiroga"
__version__ = "19/Sep/2017"


def factorial(n):
    # Local variable
    answer = n

    # Loop that iterates through all numbers that are smaller than n but bigger than 0
    for i in range(1, n):
        answer *= i

    return answer


def permutations(n, k):
    # Uses the factorial function to perform the equation: n!/(n-k)!
    return factorial(n) / factorial((n - k))


def combinations(n, k):
    # Uses the permutation funtion to perform the equation: nPk / k!
    return permutations(n, k) / factorial(k)


# Tests for quality assurance ;)
print factorial(9)
print permutations(6, 3)
print combinations(5, 2)
