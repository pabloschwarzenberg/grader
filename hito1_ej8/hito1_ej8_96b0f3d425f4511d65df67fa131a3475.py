#Descomponer un número
numero = float(input("Ingresa un valor de 4 cifras: "))


# Calculos

numero_mil = int(numero//1000)

numero_centena = numero % 1000

centena = int(numero_centena//100)

numero_decena = numero_centena%100

decena = int(numero_decena//10)

numero_unidad = numero_decena%10

unidad = int(numero_unidad//1)

# Salida

print(numero_mil,"M + ",centena,"C + ",decena,"D + ",unidad,"U")