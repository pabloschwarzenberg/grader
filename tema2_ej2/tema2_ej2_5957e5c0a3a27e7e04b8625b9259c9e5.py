def amigos(A,B):
    lista1 = []
    lista2 = []
    suma1 = 0
    suma2 = 0
    for Num in range(1, A):
        if A % Num == 0:
            lista1.append(Num)
    for Num in lista1:
        suma1 += Num
    for Num in range(1, B):
        if B % Num == 0:
            lista2.append(Num)
    for Num in lista2:
        suma2 += Num
    if (suma2 == A) and (suma1 == B):
        return True
    else:
        return False