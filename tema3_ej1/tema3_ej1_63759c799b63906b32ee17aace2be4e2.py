def suma_divisores(n):
    listai = []
    for i in range(1, n):
        if (n % i == 0):
            listai.append(i)
    suma = 0
    for i in listai:
        suma += i
        i = i + 1
    c = 0
    verificar = False
    for i in range(1, suma + 1):
        if (suma % i) == 0:
            c = c + 1
        if c >= 3:
            verificar = True
            break
        elif (suma % i) > 0:
            return (suma, False)
    if suma == 0:
        return (suma, False)
    elif c == 2 or verificar == False:
        return (suma,True)
    elif c < 2:
        return (suma,False)