# completa el código de la función
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
 
    divisorA = 0
    for divisor in divisoresA:
        divisorA = divisorA + divisor
    print(divisorA)
    divisorB = 0
    for divisor in divisoresB:
        divisorB = divisorB + divisor
    print(divisorB)
    if divisorB == a and divisorA == b:
        return True
    else:
        return False