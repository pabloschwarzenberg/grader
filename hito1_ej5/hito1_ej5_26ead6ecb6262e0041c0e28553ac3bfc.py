def calcular_digito_verificador(rut):
    # Convertir el RUT a una cadena y eliminar cualquier caracter que no sea dígito
    rut = str(rut)
    rut = rut.replace(".", "").replace("-", "")

    # Verificar si el RUT tiene el formato correcto
    if not rut.isdigit() or len(rut) < 1:
        return "RUT inválido"

    # Calcular el dígito verificador utilizando el algoritmo de Módulo 11
    suma = 0
    multiplicador = 2
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    # Obtener el dígito verificador
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = "K"

    return digito_verificador


# Solicitar al usuario que ingrese un número de RUT
numero_rut = input("Ingrese un número de RUT (sin puntos ni guiones): ")

# Calcular el dígito verificador
digito_verificador = calcular_digito_verificador(numero_rut)

# Imprimir el resultado en pantalla
print("dv =", digito_verificador)
