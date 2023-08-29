# completa el código de la función
def amigos(numero_uno, numero_dos):
    sumaUno = 0
    sumaDos = 0
    lista_divisores_uno = []
    lista_divisores_dos = []
    for i in range(numero_uno, 0, -1):
        if numero_uno % i == 0:
            lista_divisores_uno.append(i)

    for j in range(numero_dos, 0, -1):
        if numero_dos % j == 0:
            lista_divisores_dos.append(j)

    lista_divisores_dos.pop(0)
    lista_divisores_uno.pop(0)

    for k in lista_divisores_uno:
        sumaUno = sumaUno + k

    for l in lista_divisores_dos:
        sumaDos = sumaDos + l

    if sumaUno == 1 or sumaDos == 2 or sumaUno == 2 or sumaDos == 1:
        return False
    else:
        if sumaDos == numero_uno or sumaUno == numero_dos:
            return True

        else:
            return False
