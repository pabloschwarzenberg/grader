#Descomponer un número
# Solicitar un número al usuario
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Verificar que el número sea válido
if numero < 0 or numero > 9999:
    print("El número ingresado no es válido.")
else:
    # Descomponer el número en unidades, decenas, centenas y miles
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    # Imprimir la descomposición del número
    print("Descomposición del número:")
    print("Unidades:", unidades)
    print("Decenas:", decenas)
    print("Centenas:", centenas)
    print("Miles:", miles)
      