#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut_str = str(rut)  # Convertir el RUT a cadena
    rut_reverso = rut_str[::-1]  # Revertir el RUT

    factor = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return "K"
    else:
        return digito_verificador

# Solicitar el RUT al usuario
rut = int(input("Ingrese el RUT (sin dígito verificador): "))

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Mostrar el resultado
print("dv =", dv)
     