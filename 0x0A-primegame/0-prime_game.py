#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """Function to determain the winner in prime game"""

    # Counter for Maria's wins
    mariaWinsCount = 0
    # Counter for Ben's wins
    benWinsCount = 0
    for num in nums:
        # List of numbers from 1 to num
        roundsSet = list(range(1, num + 1))
        # List of prime numbers from 1 to num
        primesSet = primes_in_range(1, num)
        # If no primes, Ben automatically wins
        if not primesSet:
            benWinsCount += 1
            continue

        # Boolean to track whose turn it is
        isMariaTurns = True

        while(True):
            # If no primes left, determine the winner of the round
            if not primesSet:
                if isMariaTurns:
                    # Ben wins if it was Maria's turn and no primes left
                    benWinsCount += 1
                else:
                    # Maria wins if it was Ben's turn and no primes left
                    mariaWinsCount += 1
                break  # Exit the loop

            # Remove the smallest prime from the list
            smallestPrime = primesSet.pop(0)

            # Remove the smallest prime from the rounds set
            roundsSet.remove(smallestPrime)

            # Remove all multiples of the smallest prime from the rounds set
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            # Switch turns between Maria and Ben
            isMariaTurns = not isMariaTurns

    # Determine the overall winner
    if mariaWinsCount > benWinsCount:
        return "Maria"
    if mariaWinsCount < benWinsCount:
        return "Ben"

    # Return None if it's a tie
    return None


def is_prime(n):
    """True if n is prime, else False."""
    # If n is less than 2, it is not a prime number
    if n < 2:
        return False

    # Check divisibility up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # n is a prime number
    return True


def primes_in_range(start, end):
    """a list of prime numbers between start and end (inclusive)."""
    # List comprehension to find primes in the given range
    primes = [n for n in range(start, end + 1) if is_prime(n)]

    # Return the list of primes
    return primes
