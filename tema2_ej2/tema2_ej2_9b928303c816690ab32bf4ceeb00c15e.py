# completa el código de la función:
def amigos(A,B):
    lista1 = []
    lista2 = []
    suma1 = 0
    suma2 = 0
    for x in range(1, A):
        if A % x == 0:
            lista1.append(x)
    for x in lista1:
        suma1 += x
    for x in range(1, B):
        if B % x == 0:
            lista2.append(x)
    for x in lista2:
        suma2 += x
    if (suma2 == A) and (suma1 == B):
        return True
    else:
        return False
 
