#Descomponer un número
numero = int(input())

unidadmil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print("%i" % unidadmil, "M+", "%i" % centenas, "C+", "%i" % decenas ,"D+", "%i" % unidades, "U")