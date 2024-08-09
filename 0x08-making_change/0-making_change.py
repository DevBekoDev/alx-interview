#!/usr/bin/python3
""" Making changes """

def makeChange(coins, total):
    """ Calculate the minimum number of coins needed for the total

    Args:
        coins (list): Coin denominations available
        total (int): Amount needed
    """
    if total <= 0:  # No coins needed for zero or less
        return 0
    
    coins.sort(reverse=True)  # Sort coins from largest to smallest
    
    check = 0
    temp = 0    
    for i in coins:
        while check < total:  # Add coins until total is reached or exceeded
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i  # If total is exceeded, remove the last coin
        temp -= 1
    
    return -1  # If total can't be reached, return -1
