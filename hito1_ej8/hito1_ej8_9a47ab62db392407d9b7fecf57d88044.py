#Descomponer un número
numero = int(input())

umil = numero / 1000
tmp = numero % 1000

c = tmp / 100
tmp = tmp % 100

d = tmp / 10
unidades = tmp % 10

print("%i" % umil,"M+","%i" % c,"C+","%i" % d,"D+","%i" % unidades,"U")      