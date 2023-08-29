#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)
    rut_reversed = rut_str[::-1]
    multiplicador = 2
    suma = 0

    for digito in rut_reversed:
        suma += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        return 'k'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)

# Pedir al usuario que ingrese un número de RUT
rut = int(input("Ingresa un número de RUT: "))

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)
      