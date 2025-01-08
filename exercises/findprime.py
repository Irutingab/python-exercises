def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):  # Check up to the square root of n
        if n % i == 0:
            return False  # If n is divisible by any number, it's not prime
    return True  # If no divisors were found, the number is prime

# Test the function
number = 31
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
