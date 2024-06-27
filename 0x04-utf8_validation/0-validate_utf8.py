#!/usr/bin/python3
"""
Validate UTF8
"""


def validUTF8(data):
    """
    Validate if data contains valid UTF-8 characters
    """
    isFirstByte = True  # check if we processing the first byte of a character
    remainingBytes = 0  # Number of remaining bytes for the current character
    binaryData = []

    # Convert each integer in data to its 8-bit binary representation
    for number in data:
        binaryData.append('{0:08b}'.format(number & 255))

    # Process each binary string in binaryData
    for binary in binaryData:
        # Count the leading 1's in the binary string
        currentByteCount = countLeadingOnes(binary)

        if isFirstByte:
            # If it's the first byte, determine the expected length of the
            # character
            if currentByteCount == 0:
                continue  # Single-byte character, continue to next byte

            if 2 <= currentByteCount <= 4:
                remainingBytes = currentByteCount - 1
                isFirstByte = False  # Next bytes should be continuation bytes
                continue

            return False  # Invalid first byte
        else:
            # If it's not the first byte, it should be a continuation byte
            if binary[:2] == '10':
                remainingBytes -= 1
            else:
                return False  # Invalid continuation byte

            if remainingBytes == 0:
                isFirstByte = True  # bytes of current character are processed

    return isFirstByte


def countLeadingOnes(binary):
    """
    Count the number of leading 1's in the binary string
    """
    count = 0
    for bit in binary:
        if bit == '0':
            break
        count += 1
    return count
