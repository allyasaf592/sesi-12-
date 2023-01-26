def upperCaseCount(string): 
    upper = 0
    for i in string: 
        if i.isupper(): 
            upper += 1
    return upper