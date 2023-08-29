def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]
    multiplicador = 2
    suma = 0

    for i in rut:
        suma += int(i) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return "K"
    else:
        return digito_verificador


# Ejemplo de uso
rut = input("Ingrese el Rut sin dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)
