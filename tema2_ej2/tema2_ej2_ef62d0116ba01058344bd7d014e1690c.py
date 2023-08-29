def amigos(a, b):
    divisores_a = []
    for i in range(1, a):
        if a % i == 0:
            i = divisores_a.append(i)
    divisores_b = []
    for i in range(1, b):
        if b % i == 0:
            i = divisoresB.append(i)

    print("divisor_A =", divisores_a, "\n" + "divisoresB =", divisores_b)

    ##sumar divisores
    divisorA = 0
    for divisor in divisores_a:
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
   