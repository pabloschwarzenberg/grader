def amigos(a, b):
    divisoresA = []
    for i in range(1, a):
        if a%i == 0:
            i = divisoresA.append(i)
    divisoresB = []
    for i in range(1, b):
        if b%i == 0:
            i = divisoresB.append(i)

    print("divisoresA =", divisoresA, "\n"+"divisoresB =", divisoresB)
    
   