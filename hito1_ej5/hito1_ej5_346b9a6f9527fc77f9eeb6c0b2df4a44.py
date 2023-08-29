def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplicador = 2
    suma = 0

    # Recorremos el RUT de derecha a izquierda y multiplicamos cada dígito por un multiplicador
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    # Calculamos el dígito verificador
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return 'K'
    else:
        return digito_verificador


rut = int(input("Ingrese un número que represente un RUT: "))

digito_verificador = calcular_digito_verificador(rut)

print("dv =", digito_verificador)
      