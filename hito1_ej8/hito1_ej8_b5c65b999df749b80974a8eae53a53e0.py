#Descomponer un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

if numero < 0 or numero > 9999:
    print("El número ingresado está fuera del rango válido.")
else:
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    descomposicion = ""

    if miles > -1:
        descomposicion += str(miles) + "M+"
    if centenas > -1:
        descomposicion += str(centenas) + "C+"
    if decenas > -1:
        descomposicion += str(decenas) + "D+"
    if unidades > -1:
        descomposicion += str(unidades) + "U"

    print(descomposicion)      