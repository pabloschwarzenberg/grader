def amigos(a, b):
    divi1= []
    for i in range(1, a):
        if a%i == 0:
            i = divi1.append(i)
    divi2 = []
    for i in range(1, b):
        if b%i == 0:
            i = divi2.append(i)
          
    divisoronly = 0
    for divisor in divi1:
        divisoronly = divisoronly + divisor
    print(divisoronly)

    divisorok = 0
    for divisor in divi2:
        divisorok = divisorok + divisor
    print(divisorok)

    if divisorok == a and divisoronly == b:
        return True
    else:
        return False