import sqaure.squarescubes as squarescubes


def frequencyofcharacters(s):
    frequency = {}
    for x in s:
        frequency[x] = frequency.get(x, 0) + 1
    return frequency

# Example 
string = "ladies and gentlemen"
result = frequencyofcharacters(string)

print("frequency per character:", result)
