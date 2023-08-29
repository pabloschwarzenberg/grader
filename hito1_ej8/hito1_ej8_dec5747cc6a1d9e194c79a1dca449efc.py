#Descomponer un número
def obtener_descarga(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000

    descarga = ""
    if miles > 0:
        descarga += str(miles) + "M + "
    if centenas > 0:
        descarga += str(centenas) + "C + "
    if decenas > 0:
        descarga += str(decenas) + "D + "
    if unidades > 0:
        descarga += str(unidades) + "U"

    return descarga

# Solicitar al usuario ingresar un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Obtener la descarga en unidades, decenas, centenas y miles
descarga = obtener_descarga(numero)

# Imprimir el resultado
print("Descarga:", descarga)
      