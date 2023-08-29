# completa el código de la función
def amigos(a, b):
    divisores_A = []
    for i in range(1, a):
        if a%i == 0:
            i = divisores_A.append(i)
    divisores_B = []
    for i in range(1, b):
        if b%i == 0:
            i = divisores_B.append(i)

    print("divisoresA =", divisores_A, "\n"+"divisoresB =", divisores_B)

    divisordeA = 0
    for divisor in divisores_A:
        divisordeA = divisordeA + divisor

    divisordeB = 0
    for divisor in divisores_B:
        divisordeB = divisordeB + divisor

    if divisordeB == a and divisordeA == b:
        return True
    else:
        return False