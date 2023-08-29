def calcular_digito_verificador(rut):
    rut = str(rut)
    multiplicador = 2
    suma = 0

    # Calcula la suma ponderada del RUT en reversa
    for i in reversed(range(len(rut))):
        suma += int(rut[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    # Calcula el dígito verificador como el complemento de la suma módulo 11
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador

# Ejemplo de uso
rut = input("Ingrese el número de RUT sin dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv =", digito_verificador)