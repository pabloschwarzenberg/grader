# Obtener el número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Descomponer en unidades, decenas, centenas y miles
unidades = int(numero[-1])
decenas = int(numero[-2]) if len(numero) >= 2 else 0
centenas = int(numero[-3]) if len(numero) >= 3 else 0
miles = int(numero[-4]) if len(numero) >= 4 else 0

# Imprimir la descomposición
descomposicion = "{}M + {}C + {}D + {}U".format(miles, centenas, decenas, unidades)
print(descomposicion)

      