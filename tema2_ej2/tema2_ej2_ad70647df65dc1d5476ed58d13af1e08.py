def amigos(a, b):
    divisoresA = []
    for i in range(1, a):
        if a % i == 0:
            divisoresA.append(i)
    
    divisoresB = []
    for i in range(1, b):
        if b % i == 0:
            divisoresB.append(i)
    
    print("divisoresA =", divisoresA)
    print("divisoresB =", divisoresB)

    # Summing the divisors
    divisorA = sum(divisoresA)
    print(divisorA)
    divisorB = sum(divisoresB)
    print(divisorB)

    if divisorB == a and divisorA == b:
        return True
    else:
        return False
