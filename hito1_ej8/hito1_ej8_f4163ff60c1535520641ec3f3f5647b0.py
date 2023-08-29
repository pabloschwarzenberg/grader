#Descomponer un numero
numero = input("Ingrese un numero: ")
num = ''
for i in range(-len(numero), 0, 1):
    if i == -1:
        unidades = ("{0}U".format(numero[-1]))
        num += ("{0}".format(unidades))
    if i == -2:
        decenas = ("{0}D ".format(numero[-2]))
        num += ("{0}+ ".format(decenas))
    if i == -3:
        centenas = ("{0}C ".format(numero[-3]))
        num += ("{0}+ ".format(centenas))
    if i == -4:
        miles = ("{0}M ".format(numero[-4]))
        num += ("{0}+ ".format(miles))
print(num)