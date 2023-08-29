#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)
    rut = rut.replace(".", "")  # Eliminar los puntos del RUT (opcional)

    # Multiplicar cada dígito del RUT por los números de la serie y sumar los productos
    multiplicador = [2, 3, 4, 5, 6, 7]
    suma = 0
    indice_multiplicador = 0

    for i in range(len(rut) - 1, -1, -1):
        digito = int(rut[i])
        producto = digito * multiplicador[indice_multiplicador]
        suma += producto
        indice_multiplicador = (indice_multiplicador + 1) % 6

    # Calcular el módulo 11 y el dígito verificador
    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        digito_verificador = "0"
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador


# Ejemplo de uso
rut = input("Ingresa el RUT sin guion ni dígito verificador: ")
digito_verificador = calcular_digito_verificador(rut)
print("dv=" + str(digito_verificador))