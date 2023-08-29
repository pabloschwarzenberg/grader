#Descomponer un número
n = int(input('Ingrese numero: '))

m = (n // 1000)
n = n - m * 1000

c = n // 100
n = n - c * 100

d = n // 10

u = n - d * 10
if m != 0:
    print(m, "M+", c, "C+", d, 'D+', u, "U")
elif c != 0:
    print(c,"C+",d,'D+',u,"U")
elif d != 0:
    print(d, 'D+', u, "U")
elif u != 0:
    print(u, "U")