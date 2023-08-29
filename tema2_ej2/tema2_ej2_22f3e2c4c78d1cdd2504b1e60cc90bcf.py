def verificar_amigos(a, b):
    arrA = []
    arrB = []
    if(a == b):
        return False
    for i in range(2, a):
        if a % i == 0:
            arrA.append(i)
    amigosA = sum(arrA)
    if(amigosA == 0): 
        return False

    for i in range(2, b):
        if b % i == 0:
            arrB.append(i)

    amigosB = sum(arrB)
    if(amigosB == 0): 
        return False
    
    if(amigosA == amigosB):
        return True
    else: 
        return False
