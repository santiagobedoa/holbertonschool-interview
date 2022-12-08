#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes
More info:
- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Description:
    Write a method that determines if all the boxes can be opened
    Arguments:
    boxes --> List of Lists, it contains the boxes with keys
    Return boolean
    Variables:
    myKeys --> List, Store the number keys to open boxes
    key --> integer, key of the myKeys
    boxKey --> integer, key inside of an specific box
    """
    keys = [0]
    for key in keys:
        box = boxes[key]
        for key_in_box in box:
            if key_in_box not in keys and key_in_box < len(boxes):
                keys.append(key_in_box)
    if len(keys) == len(boxes):
        return True
    return False
