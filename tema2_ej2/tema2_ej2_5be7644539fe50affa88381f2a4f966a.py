def amigos(a,b):
    divisores1 = []
    divisores2 = []
    indice = 0
    resultado = 0
    suma_b = 0
    contador = 0
    for i in range(1,a):
        if a % i ==0:
            divisores1.append(i)
    for j in range(1,b):
        if b % j == 0:
            divisores2.append(j)
    while indice < len(divisores1):
        resultado = resultado + divisores1[indice]
        indice = indice + 1
    while contador < len(divisores2):
        suma_b= suma_b + divisores2[contador]
        contador = contador + 1
    if resultado == b and suma_b == a:
        print("Son Amigos")
        return True
    else:
        print("No son Amigos")
        return False           