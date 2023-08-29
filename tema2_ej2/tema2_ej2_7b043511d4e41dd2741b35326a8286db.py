def amigos(numA, numB):
    
    dividersA = []
    for i in range(1, numA):
        if numA%i == 0:
            i = dividersA.append(i)

    dividersB = []
    for i in range(1, numB):
        if numB%i == 0:
            i = dividersB.append(i)

    dividerA = 0
    for x in dividersA:
        dividerA += x
    print(dividerA)

    dividerB = 0
    for y in dividersB:
        dividerB += y
    print(dividerB)

    if(dividerB == numA and dividerA == numB):
        areFriends = True
    else:
        areFriends = False

    return areFriends