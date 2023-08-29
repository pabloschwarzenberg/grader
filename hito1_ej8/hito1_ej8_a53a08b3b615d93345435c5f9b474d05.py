#Descomponer un número
def descomponer_numero(numero):
    # Obtener los dígitos individuales
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    # Crear la cadena de descomposición
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    descomposicion += str(unidades) + "U"

    return descomposicion


# Solicitar al usuario un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Verificar si el número tiene más de 4 dígitos
if numero < 0 or numero > 9999:
    print("Número inválido. Por favor, ingrese un número entre 0 y 9999.")
else:
    # Obtener la descomposición del número
    descomposicion = descomponer_numero(numero)
    print("Descomposición:", descomposicion)