#Cálculo del dígito verificador de un rut
x = int(input("ingrese rut: "))
a = x//10000000
x = x%10000000
b = x//1000000
x = x%1000000
c = x//100000
x = x%100000
d = x//10000
x = x%10000
e = x//1000
x = x%1000
f = x//100
x = x%100
g = x//10
x = x%10
h = x//1


suma = h*2 + g*3 + f*4 + e*5 + d*6 + c*7 + b*2 + a*3

resto = suma//11
menos = suma - 11*resto
resta = 11 - menos


if resta == 11:
    print("dv=0")
elif resta == 10:
    print("dv=K")
else:
    print("dv=",resta)
