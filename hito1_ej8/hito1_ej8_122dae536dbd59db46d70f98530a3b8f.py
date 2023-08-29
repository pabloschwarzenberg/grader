#Descomponer un número
# Solicitar al usuario un número de hasta 4 dígitos
numero = int(input("Ingresa un número de hasta 4 dígitos: "))
def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000

    return miles, centenas, decenas, unidades

# Verificar si el número tiene más de 4 dígitos
if numero < 0 or numero > 9999:
    print("Número inválido. Debe ser un número de hasta 4 dígitos.")
else:
    # Obtener la descomposición del número
    miles, centenas, decenas, unidades = descomponer_numero(numero)

    # Imprimir la descomposición
    print("Unidades:", unidades)
    print("Decenas:", decenas)
    print("Centenas:", centenas)
    print("Miles:", miles)
      