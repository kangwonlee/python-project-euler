"""
Problem 003: Largest Prime Factor
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of `n`."""
    factor = 2
    largest = 1
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 1
    if n > 1:
        largest = n
    return largest


if __name__ == "__main__":
    print(largest_prime_factor(600_851_475_143))
