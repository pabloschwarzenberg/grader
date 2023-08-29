#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)  # Convertir el RUT a cadena de texto
    rut_reverso = rut_str[::-1]  # Invertir el RUT

    factor = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)

    if digito_verificador == 11:
        return "dv=0"
    elif digito_verificador == 10:
        return "dv=K"
    else:
        return "dv=" + str(digito_verificador)

# Ejemplo de uso
rut = input("Ingrese el RUT sin el dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print(digito_verificador)