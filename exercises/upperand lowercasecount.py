def String_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    
    for c in s:
        if c.isupper():  
            d["UPPER_CASE"] += 1
        elif c.islower():  
            d["LOWER_CASE"] += 1
        else:
            pass 
    print("Original string: ", s)
    print("No. of upper case characters: ", d["UPPER_CASE"])
    print("No. of lower case characters: ", d["LOWER_CASE"])

String_test("The quick Brown Fox")
