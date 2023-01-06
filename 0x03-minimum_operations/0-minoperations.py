#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def countProcess(num: int) -> list[int]:
    """
    Returns a list of the prime factors of num.

    Parameters:
    - num: An integer for which the prime factors will be calculated.

    Returns:
    - A list of the prime factors of num.
    """
    # Initialize a counter variable to 1
    counter = 1
    # Initialize an empty list to store the prime factors
    primeList = []
    # Initialize a variable to store the target num
    target = num
    # Loop until target is 1
    while target != 1:
        # Increment counter by 1
        counter += 1
        # If target is divisible by counter, enter the inner loop
        if target % counter == 0:
            while target % counter == 0 and target != 1:
                # Divide target by counter and append counter to the list of prime factors
                target /= counter
                primeList.append(counter)
    # Return the list of prime factors
    return primeList


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in a file using a text editor that can execute only two
    operations: Copy All and Paste.

    Parameters:
    - n: An integer representing the target number of H characters.

    Returns:
    - An integer representing the minimum number of operations needed to
    get to n H characters.
    - If it is not possible to get to n H characters, returns 0.
    """
    # If n is less than 2 or not an integer, return 0
    if n < 2 or type(n) is not int:
        return 0
    # Get the list of prime factors of n
    values = countProcess(n)
    # Return the sum of the elements in the list of prime factors
    return sum(values)
