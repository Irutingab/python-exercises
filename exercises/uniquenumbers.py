def Unique_Numbers(l):
    x = []
    for a in l:
        if a not in x:  # Check if the element is not already in the result list
            x.append(a)  # Add the unique element to the result list
    return x

print(Unique_Numbers([1, 2, 3, 3, 3, 3, 4, 5]))
