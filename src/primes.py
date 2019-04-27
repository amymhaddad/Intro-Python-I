"""Is a given number prime?"""

def is_prime(number):
    """Determine if a number is evenly divisble by another whole number"""

    for num in range(1, number + 1):
        if number % num == 0:
            return False
        return True

print(is_prime(15))
