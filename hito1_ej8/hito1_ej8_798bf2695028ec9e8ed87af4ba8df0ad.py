#Descomponer un número
numero = input("Ingresa un número de hasta 4 dígitos: ")

# Descomponer el número en unidades, decenas, centenas y miles
if len(numero) == 1:
    unidades = int(numero)
    decenas = 0
    centenas = 0
    miles = 0
elif len(numero) == 2:
    unidades = int(numero[-1])
    decenas = int(numero[-2])
    centenas = 0
    miles =0
elif len(numero) == 3:
    unidades = int(numero[-1])
    decenas = int(numero[-2])
    centenas = int(numero[-3])
    miles = 0
else:
 unidades = int(numero[-1])
 decenas = int(numero[-2])
 centenas = int(numero[-3])
 miles = int(numero[-4])

# Imprimir el resultado
print(miles, "M +", centenas, "C +", decenas, "D +", unidades, "U")     