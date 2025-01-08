def Factorial(n):
    if n < 0:
        return "Negatives numbers have undefined factorials"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range (2, n + 1):
            result *= i
        return result
    #example
number = 5
print(f"the factorial of {number} is : {(Factorial(number))}") 
# f-string The f-string substitutes {number} with the value of number (5) 
# and {Factorial(number)} with the output of the Factorial function for number (5).
