# completa el código de la función
def amigos(a,b):
    lista1=[]
    lista2 =[]
    s1 = 0
    s2 = 0
    for x in range(1, a):
        if a % x == 0:
            lista1.append(x)
    for x in lista1:
        s1 += x
    for x in range(1, b):
        if b % x == 0:
            lista2.append(x)
    for x in lista2:
        s2 += x
    if s1 == b and s2 == a:
        return True
    else:
        return False