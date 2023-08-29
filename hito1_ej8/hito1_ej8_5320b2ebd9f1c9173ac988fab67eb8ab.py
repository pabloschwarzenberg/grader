#Descomponer un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

miles = numero // 1000
centenas = (numero % 1000) // 100
decenas = (numero % 100) // 10
unidades = numero % 10

resultado = []
if miles > 0 or numero >= 1000:
    resultado.append("{}M".format(miles))
if centenas > 0 or numero >= 100:
    resultado.append("{}C".format(centenas))
if decenas > 0 or numero >= 10:
    resultado.append("{}D".format(decenas))
resultado.append("{}U".format(unidades))

print(" + ".join(resultado))
