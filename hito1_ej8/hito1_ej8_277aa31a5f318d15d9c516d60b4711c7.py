#Descomponer un número
numero = int(input("Ingrese un numero de hasta 4 digitos: "))

if numero < 0 or numero > 9999:
    print("El numero ingresado esta fuera del rango valido.")
else:
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    descomposicion = ""

    if miles >= 0:
        descomposicion += str(miles) + "M + "
    if centenas >= 0:
        descomposicion += str(centenas) + "C + "
    if decenas >= 0:
        descomposicion += str(decenas) + "D + "
    if unidades >= 0:
        descomposicion += str(unidades) + "U"

    if descomposicion.endswith(" + "):
        descomposicion = descomposicion[:-3]

    print("Descomposicion:", descomposicion)      