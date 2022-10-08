"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes need to be more than 0!")
        
    list = []
    list.append(2)

    while len(list) < number_of_primes:
        foundNextPrime = False
        nextNumberToCheck = list[-1]

        while(not foundNextPrime):
            nextNumberToCheck += 1
            foundNextPrime = isPrime(nextNumberToCheck)

        list.append(nextNumberToCheck)

    return list


def isPrime(number):
    prime = True
    i = 2

    while i < number and prime:
        if(number % i == 0):
            prime = False
        i += 1

    return prime
