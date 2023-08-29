def amigos(a, f):
    suma1 = 0
    suma2 = 0
    rango1 = []
    rango2 = []

    # Establecer el rango pa el primer numero
    for i in range(1, a):
        if a % i == 0:
            rango1.append(i)

    # Coloca la condicion
    for i in rango1:
        suma1 += i

    # Establecer el rango para el segundo numero
    for i in range(1, f):
        if f % i == 0:
            rango2.append(i)

    # Colocar la condicion
    for i in rango2:
        suma2 += i

    # Condicion de los dos numeros son iguales
    if suma1 == f and suma2 == a:
        print(True)
        return 1
    else:
        print(False)
        return 0
        

       


 