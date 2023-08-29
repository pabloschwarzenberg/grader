#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_reversed = str(rut)[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0

    for digito in rut_reversed:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        digito_verificador = 'K'
    elif digito_verificador == 11:
        digito_verificador = 0

    return digito_verificador

# Solicitar al usuario que ingrese un número de RUT
rut = int(input("Ingrese un número de RUT: "))

# Calcular el dígito verificador llamando a la función
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)
     