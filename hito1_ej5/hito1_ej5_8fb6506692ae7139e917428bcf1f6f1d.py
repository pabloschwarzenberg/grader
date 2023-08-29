#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)  # Convertir el RUT a una cadena de caracteres
    rut_reverso = rut_str[::-1]  # Invertir el orden de los caracteres
    factor = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Solicitar el RUT al usuario
rut = int(input("Ingrese un RUT sin el dígito verificador: "))

# Llamar a la función y mostrar el resultado
dv = calcular_digito_verificador(rut)
print("dv =", dv)
