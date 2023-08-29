def amigos(a,b):
    divisores1 = []
    divisores2 = []
    suma1 = 0
    suma2 = 0
    for i in range(a):
        if a % (i+1) == 0:
            divisores1.append(i+1)
    if len(divisores1) != 0:
        divisores1.pop()
    for i in divisores1:
        suma1 += i
    for i in range(b):
        if b % (i+1) == 0:
            divisores2.append(i+1)
    if len(divisores2) != 0:
        divisores2.pop()
    for i in divisores2:
        suma2 += i
    if suma1 == b and suma2 == a:
        return True
    else:
        return False