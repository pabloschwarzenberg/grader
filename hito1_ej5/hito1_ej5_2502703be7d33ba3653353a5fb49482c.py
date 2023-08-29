#Cálculo del dígito verificador de un rut

def calcular_digito_verificador(rut):
    rut = str(rut)
    rut_reverso = rut[::-1]  # Invertir el RUT
    multiplicador = 2
    suma = 0

    for digito in rut_reverso:
        suma += int(digito) * multiplicador
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

# Solicitar entrada al usuario
rut = input("Ingrese el RUT (sin dígito verificador): ")

# Calcular dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir resultado
print("dv =", dv)
