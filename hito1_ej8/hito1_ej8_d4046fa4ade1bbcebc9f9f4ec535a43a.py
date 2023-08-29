#Descomponer un número
numero = int(input("Ingresa un número entre 0 y 9999: "))

# Validar que el número esté en el rango correcto
if numero < 0 or numero > 9999:
    print("El número ingresado está fuera del rango permitido.")
else:
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    descomposicion = ""

    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    descomposicion += str(unidades) + "U"

    print("Descomposición:", descomposicion)
