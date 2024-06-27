#!/usr/bin/python3
"""
validate if a sequance of input follows the utf-8 encoding pattern
"""


def validUTF8(data):
    """
    validate if data are UTF8 chars
    """
    n = len(data)
    next = 0
    for i in data:
        if next == 0:
            if (i >> 5) == 0b110:  # for 2 bytes
                next = 1
            elif (i >> 4) == 0b1110:  # for 3 bytes
                next = 2
            elif (i >> 3) == 0b11110:  # for 4 bytes
                next = 3
            elif (i >> 7) != 0b0:
                return False
        else:
            if (i >> 6) != 0b10:  # checking next occurence
                return False
            next -= 1
    if next == 0:
        return True
    return False
