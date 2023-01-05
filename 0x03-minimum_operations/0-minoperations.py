#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    target = n
    # edge case: if n is 0 or 1, we can't perform any operations
    if n <= 1:
        return 0

    # find the largest power of 2 that is less than or equal to n
    num_operations = 0
    while n > 1:
        n //= 2
        num_operations += 1

    # perform Paste operations to reach the desired number of H characters
    num_pastes = 0
    while n < target:
        n *= 2
        num_pastes += 1

    return num_operations + num_pastes
