#Descomponer un número
numero = int(input("ingrese numero de cuatro digitos: "))

m = numero / 1000
tmp = numero % 1000

c = tmp / 100
tmp = tmp % 100

d = tmp / 10
tmp = tmp % 10

u = numero%10


x = ("%i M" % m)
y = ("%i C" % c)
z = ("%i D" % d)
j = ("%i U" % u)

print("{} + {} + {} + {}". format(x, y, z, j))      