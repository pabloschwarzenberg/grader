#Descomponer un número
numero = int(input("ingrese un numero : "))

umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print ("la descomposicion es: %im" % umil, " + %ic" % centenas,  "+ %id" % decenas, " + %iu" % unidades)