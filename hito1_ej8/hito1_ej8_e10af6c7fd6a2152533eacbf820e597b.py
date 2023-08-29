#Descomponer un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Verificar si el número tiene más de 4 dígitos
if numero < 0 or numero > 9999:
    print("El número debe tener como máximo 4 dígitos y ser mayor o igual a cero.")
else:
    unidades = numero % 10
    decenas = (numero % 100) // 10
    centenas = (numero % 1000) // 100
    miles = numero // 1000

    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    descomposicion += str(unidades) + "U"

    print("Descomposición:", descomposicion)
