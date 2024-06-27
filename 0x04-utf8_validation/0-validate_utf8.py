#!/usr/bin/python3
"""
check a seqance of an inpit is utf-8 valid
"""


def validUTF8(data):
    """
    using the bit manipualtion to validate utf8 encoding
    """

    count = 0
    for n in data:
        if count == 0:
            if (n >> 7) == 0:
                count = 0
            elif (n >> 5) == 0x06:
                count = 1
            elif (n >> 4) == 0x0e:
                count = 2
            elif (n >> 3) == 0x1e:
                count = 3
            else:
                return False
        else:
            if (n >> 6) != 0x02:
                return False
            count -= 1
    return count == 0
