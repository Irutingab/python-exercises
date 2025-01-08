import pesonattributes
def SquareAndCubes(numbers):
    result = {}
    for number in numbers:
        result[number] = {
            "square": number ** 2,
            "cube": number ** 3
        }
    return result

numbers = [1, 2, 3, 4, 5]
output = SquareAndCubes(numbers)
print("Squares and Cubes:", output)
