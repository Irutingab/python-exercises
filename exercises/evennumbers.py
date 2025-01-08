def print_even_numbers(lst):
    # Loop through the list and print even numbers
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            print(num, end=" ")

# Sample list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Call the function
print("Even numbers in the list:")
print_even_numbers(sample_list)
