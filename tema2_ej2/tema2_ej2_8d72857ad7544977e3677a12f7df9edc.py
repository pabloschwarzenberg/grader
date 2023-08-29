# completa el código de la función
def amigos(a, b):
    divisorA = []
    for i in range(1, a):
        if a%i == 0:
            i = divisorA.append(i)
    divisorB = []
    for i in range(1, b):
        if b%i == 0:
            i = divisorB.append(i)

    print("divisoresA =", divisorA, "\n"+"divisoresB =", divisorB)
    
    ##sumar divisores
    divisoresA = 0
    for divisor in divisorA:
        divisoresA = divisoresA + divisor
    print(divisoresA)

    divisoresB = 0
    for divisor in divisorB:
        divisoresB = divisoresB + divisor
    print(divisoresB)

    if divisoresB == a and divisoresA == b:
        return True
    else:
        return False