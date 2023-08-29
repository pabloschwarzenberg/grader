rut = input("Ingresa un rut: ")

lista_rut = list(map(int, rut))
lista_rut.reverse()

if len(rut) == 8:   # [1,1,2,6,3,0,6,2]

    lista_1 = lista_rut[:-2]
    lista_2 = lista_rut[-2:]

    multiplicador_1 = 2
    sumador_1 = 0
    while multiplicador_1 != 7:
        for numero_1 in lista_1:
            producto_1 = numero_1 * multiplicador_1
            sumador_1 = sumador_1 + producto_1
            #print(f"{numero_1} * {multiplicador_1} = {sumador_1}")
            multiplicador_1 = multiplicador_1 + 1
        #print(sumador_1)
        multiplicador_1 = 7

    multiplicador_2 = 2
    sumador_2 = 0
    while multiplicador_2 != 3:
        for numero_2 in lista_2:
            producto_2 = numero_2 * multiplicador_2
            sumador_2 = sumador_2 + producto_2
            #print(f"{numero_2} * {multiplicador_2} = {sumador_2}")
            multiplicador_2 = multiplicador_2 + 1
        #print(sumador_2)
        multiplicador_2 = 3

    suma_total = sumador_1 + sumador_2
    modulo = suma_total % 11
    digito_verificador = 11 - modulo

    if digito_verificador == 11:
        digito_verificador = 0
        print("dv = ",digito_verificador)

    elif digito_verificador == 10:
        digito_verificador = "K"
        print("dv = ",digito_verificador)

    else:
        print("dv = ",digito_verificador)


elif len(rut) == 7: # [5,7,6,6,5,8,1]

    lista_1 = lista_rut[:-1]
    lista_2 = lista_rut[-1:]

    multiplicador_1 = 2
    sumador_1 = 0
    while multiplicador_1 != 7:
        for numero_1 in lista_1:
            producto_1 = numero_1 * multiplicador_1
            sumador_1 = sumador_1 + producto_1
            #print(f"{numero_1} * {multiplicador_1} = {sumador_1}")
            multiplicador_1 = multiplicador_1 + 1
        #print(sumador_1)
        multiplicador_1 = 7

    multiplicador_2 = 2
    sumador_2 = 0
    while multiplicador_2 != 3:
        for numero_2 in lista_2:
            producto_2 = numero_2 * multiplicador_2
            sumador_2 = sumador_2 + producto_2
            #print(f"{numero_2} * {multiplicador_2} = {sumador_2}")
            multiplicador_2 = multiplicador_2 + 1
        #print(sumador_2)
        multiplicador_2 = 3

    suma_total = sumador_1 + sumador_2
    modulo = suma_total % 11
    digito_verificador = 11 - modulo

    if digito_verificador == 11:
        digito_verificador = 0
        print("dv = ",digito_verificador)

    elif digito_verificador == 10:
        digito_verificador = "K"
        print("dv = ",digito_verificador)

    else:
        print("dv = ",digito_verificador)