#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a cadena
    rut = rut.zfill(8)  # Rellenar con ceros a la izquierda si el RUT tiene menos de 8 dígitos

    factor = 2
    suma = 0

    # Calcular la suma ponderada de los dígitos del RUT de derecha a izquierda
    for i in range(len(rut)-1, -1, -1):
        suma += int(rut[i]) * factor
        factor += 1
        if factor == 8:
            factor = 2

    # Calcular el dígito verificador
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'K'

    return digito_verificador

# Pedir al usuario que ingrese un número de RUT
numero_rut = int(input("Ingrese un número de RUT: "))

# Calcular el dígito verificador
dv = calcular_digito_verificador(numero_rut)

# Mostrar el resultado
print("dv =", dv)

     