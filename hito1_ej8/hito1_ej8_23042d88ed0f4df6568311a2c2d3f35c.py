def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    return unidades, decenas, centenas, miles

# Solicitar entrada al usuario
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Llamar a la función y obtener los resultados
unidades, decenas, centenas, miles = descomponer_numero(numero)

# Mostrar los resultados
print("{}M+{}C+{}D+{}U".format(miles, centenas, decenas, unidades))
