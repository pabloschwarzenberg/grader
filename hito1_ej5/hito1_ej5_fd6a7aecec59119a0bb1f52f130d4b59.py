#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut[::-1]  # Invertir el RUT

    multiplicador = 2
    suma = 0

    for d in rut:
        suma += int(d) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Solicitar el RUT al usuario
rut = input("Ingrese el RUT sin dígito verificador: ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)
