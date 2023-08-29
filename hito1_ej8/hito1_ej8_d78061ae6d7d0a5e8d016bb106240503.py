#Descomponer un número
def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    return miles, centenas, decenas, unidades

numero = int(input("Ingrese un número de hasta 4 dígitos: "))

if numero < 0 or numero > 9999:
    print("El número ingresado está fuera del rango válido.")
else:
    miles, centenas, decenas, unidades = descomponer_numero(numero)

    descomposicion = ""

    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    descomposicion += str(unidades) + "U"

    print(descomposicion)
