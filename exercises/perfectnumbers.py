def is_perfect_number(n):
    if n <= 0:
        return False  # Perfect numbers are positive integers
    divisors_sum = 0
    # Find the sum of proper divisors of n (excluding the number itself)
    for i in range(1, n):
        if n % i == 0:  # If i is a divisor of n
            divisors_sum += i
    # Check if the sum of divisors equals the number itself
    return divisors_sum == n

# Test the function
number = 24
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
