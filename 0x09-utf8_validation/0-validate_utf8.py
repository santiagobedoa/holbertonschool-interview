#!/usr/bin/python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    """
    bit1 checks if significant byte is 1
    bit2 checks if second significant byte is 0
    nbytes keeps track of how many 1s before 0 occurs
    data represented by a list of integers to check
    """

    # Define the bit masks and counters
    bit1 = 1 << 7  # 0b10000000
    bit2 = 1 << 6  # 0b01000000
    nbytes = 0

    # If the data is empty, return True
    if not data or len(data) == 0:
        return True

    # Iterate over the data and check each byte
    for num in data:
        bit = 1 << 7
        if nbytes == 0:
            # Check how many bytes there are in the current sequence
            while bit & num:
                nbytes += 1
                bit = bit >> 1

            # If there are no bytes or too many, return False
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            # If this is not the first byte in the sequence, check if it has the right bit pattern
            if not (num & bit1 and not (num & bit2)):
                return False

        # Decrement the byte counter
        nbytes -= 1

    # If the counter is not zero at the end, return False
    if nbytes:
        return False
    else:
        return True
