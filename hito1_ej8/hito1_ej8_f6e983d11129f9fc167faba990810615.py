#Descomponer un número
numero = int(input("Ingrese Numero hasta 4 digitos: "))

umil = numero / 1000

tmp = numero % 1000

centenas = tmp / 100

tmp = tmp % 100

decenas = tmp / 10


print("Unidades de mil: %i" % umil)

print("Centenas: %i" % centenas)

print("Decenas: %i" % decenas)





      