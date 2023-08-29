#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a una cadena de texto

    # Obtener el número de RUT
    num = rut[:-1]

    # Calcular la suma de productos
    factor = 2
    suma = 0

    # Recorrer el número de RUT de derecha a izquierda
    for i in reversed(num):
        suma += int(i) * factor
        factor += 1
        if factor > 7:
            factor = 2

    # Calcular el dígito verificador
    verificador_esperado = 11 - (suma % 11)
    if verificador_esperado == 11:
        verificador_esperado = "0"
    elif verificador_esperado == 10:
        verificador_esperado = "K"

    return verificador_esperado


# Ejemplo de uso
rut_ingresado = input("Ingrese el número de RUT: ")
dv_calculado = calcular_digito_verificador(rut_ingresado)
print("dv=" + str(dv_calculado))

    