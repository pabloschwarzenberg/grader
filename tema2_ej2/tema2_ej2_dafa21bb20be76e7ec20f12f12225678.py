# completa el código de la función
def amigos(a,b):
  return
def amigos(a,b):
    suma_a = 0
    suma_b = 0
    lista_b = []
    lista_a = []
    for i in range(1,a):
        resto = a % i
        if resto == 0:
            lista_a.append(i)
    for j in range(1,b):
        resto = b % j
        if resto == 0:
            lista_b.append(j)
    for k in lista_a:
        suma_a = suma_a + k

    for p in lista_a:
        suma_b = suma_b + p

    if suma_a == b or suma_b == a:
        return True
    else:
        return False          