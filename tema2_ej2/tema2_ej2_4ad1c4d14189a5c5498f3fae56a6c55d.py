# completa el código de la función
def amigos(a,b):
    lista_a = []
    lista_b = []
    for i in range(1,a+1):
        if (a%i) == 0:
            lista_a.append(i)
    for i in range(1,b+1):
        if (b%i) == 0:
            lista_b.append(i)

    lista_a.remove(lista_a[-1])
    lista_b.remove(lista_b[-1])
    
    suma_a = 0
    for i in lista_a:
        suma_a = suma_a + i
    suma_b = 0
    for i in lista_b:
        suma_b = suma_b + i

    if (a == suma_b) and (b == suma_a):
        return True
    else:
        return False
           