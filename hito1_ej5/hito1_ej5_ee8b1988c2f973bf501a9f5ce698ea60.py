# Solicitar el número de Rut al usuario
rut = input("Ingrese el número de Rut (sin dígito verificador): ")

# Verificar que el Rut tenga al menos un dígito
if len(rut) == 0:
    print("El Rut ingresado no es válido.")
else:
    # Calcular el dígito verificador
    suma = 0
    multiplicador = 2
    for digito in reversed(rut):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    digito_verificador = 11 - (suma % 11)

    # Ajustar el dígito verificador si es 11 o 10
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    # Imprimir el resultado
    print("dv =", digito_verificador)
