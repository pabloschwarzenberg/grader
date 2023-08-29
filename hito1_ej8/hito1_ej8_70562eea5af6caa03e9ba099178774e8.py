#Descomponer un número
numero = int(input())

m = numero / 1000
tm = numero % 1000

c = tm / 100
tm = tm % 100

d = tm / 10
u = tm % 10

print("%i" % m, "M+", "%i" % c, "C+", "%i" % d, "D+", "%i" % u, "U")