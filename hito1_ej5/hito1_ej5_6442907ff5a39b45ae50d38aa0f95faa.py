def calcular_digito_verificador(rut):
    rut = str(rut)

    if len(rut) == 0:
        return "RUT inválido"

    rut = rut.replace(".", "").replace("-", "")

    if len(rut) < 2:
        return "RUT inválido"

    numero = rut[:-1]
    digito_verificador = rut[-1]

    factor = 2
    suma = 0

    for digito in reversed(numero):
        suma += int(digito) * factor
        factor += 1

        if factor > 7:
            factor = 2

    digito_esperado = 11 - (suma % 11)

    if digito_esperado == 11:
        digito_esperado = "0"
    elif digito_esperado == 10:
        digito_esperado = "K"
    else:
        digito_esperado = str(digito_esperado)

    if digito_verificador.upper() == digito_esperado:
        return "dv=" + digito_verificador
    else:
        return "Dígito verificador incorrecto"

rut = input("Ingrese un número de RUT: ")

resultado = calcular_digito_verificador(rut)

print(resultado)