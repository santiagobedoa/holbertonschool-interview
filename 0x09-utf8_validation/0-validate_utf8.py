#!/usr/bin/env python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    """
    bit1 checks if significant byte is 1
    bit2 checks if second significant byte is 0
    nbytes keeps track of how many 1s before 0 occurs
    data represented by a list of integers to check
    """
    # Count the number of leading 1 bits in the first byte of the current char
    num_bytes = 0
    for i in range(8):
        if data[0] & (1 << (7 - i)) == 0:
            break
        num_bytes += 1

    # Check that the remaining bytes are of the form 10xxxxxx
    if num_bytes > 1:
        for j in range(1, num_bytes):
            if j >= len(data) or (data[j] & 0b11000000) != 0b10000000:
                return False

    # Check that the first byte is of the form:
    # 0xxxxxxx, 110xxxxx, 1110xxxx, or 11110xxx
    if num_bytes == 0:
        if data[0] & 0b10000000 != 0:
            return False
    elif num_bytes == 1:
        return False
    elif num_bytes == 2:
        if data[0] & 0b11100000 != 0b11000000:
            return False
    elif num_bytes == 3:
        if data[0] & 0b11110000 != 0b11100000:
            return False
    elif num_bytes == 4:
        if data[0] & 0b11111000 != 0b11110000:
            return False

    return True
