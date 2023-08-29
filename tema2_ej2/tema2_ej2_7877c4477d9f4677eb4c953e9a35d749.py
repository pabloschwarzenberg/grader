def amigos(a, b):
    dividersA = []
    for i in range(1, a):
        if a%i == 0:
            i = dividersA.append(i)
    dividersB = []
    for i in range(1, b):
        if b%i==0:
            i = dividersB.append(i)

    print("Divisores 1 =", dividersA, "\n"+"divisores 2 =", dividersB)
#1.Divisor-------------------------
    dividerA=0
    for divider in dividersA:
        dividerA = dividerA+divider
    print(dividerA)
#2.Divisor-------------------------
    dividerB=0
    for divider in dividersB:
        dividerB = dividerB+divider
    print(dividerB)
#Confirmador-----------------------
    if dividerB==a and dividerA==b:
        return True
    else:
        return False 