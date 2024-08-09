#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
    """Function to determain the winner in prime game"""
    mariaWinsCount = 0  # Counter for Maria's wins
    benWinsCount = 0    # Counter for Ben's wins

    for num in nums:
        roundsSet = list(range(1, num + 1))  # List of numbers from 1 to num
        primesSet = primes_in_range(1, num)  # List of prime numbers from 1 to num

        if not primesSet:  # If no primes, Ben automatically wins
            benWinsCount += 1
            continue

        isMariaTurns = True  # Boolean to track whose turn it is

        while(True):
            if not primesSet:  # If no primes left, determine the winner of the round
                if isMariaTurns:
                    benWinsCount += 1  # Ben wins if it was Maria's turn and no primes left
                else:
                    mariaWinsCount += 1  # Maria wins if it was Ben's turn and no primes left
                break  # Exit the loop

            smallestPrime = primesSet.pop(0)  # Remove the smallest prime from the list
            roundsSet.remove(smallestPrime)   # Remove the smallest prime from the rounds set

            # Remove all multiples of the smallest prime from the rounds set
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns  # Switch turns between Maria and Ben

    # Determine the overall winner
    if mariaWinsCount > benWinsCount:
        return "Maria"
    if mariaWinsCount < benWinsCount:
        return "Ben"

    return None  # Return None if it's a tie

def is_prime(n):
    """True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to the square root of n
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end + 1) if is_prime(n)]  # List comprehension to find primes
    return primes

