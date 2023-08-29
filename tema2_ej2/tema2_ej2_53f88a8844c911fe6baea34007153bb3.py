# completa el código de la función
def amigos(a,b):
    suma_a = 0
    suma_b = 0
    lista_a = []
    lista_b = []
    a=int(a)
    b=int(b)
    for i in range(1,a):
        if a%i==0:
            lista_a.append(i)
    print(lista_a)
    for i in range(1,b):
        if b%i==0:
            lista_b.append(i)
    print(lista_b)
    for x in lista_a:
        suma_a+=x
    for n in lista_b:
        suma_b+=n

    print(suma_a)
    print(suma_b)

    if suma_a==b and suma_b==a:
        return True
    else:
        return False