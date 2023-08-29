#Sistema de Ecuaciones
a = int(input("ingrese numero: "))
b = int(input("ingrese numero: "))
c = int(input("ingrese numero: "))
d = int(input("ingrese numero: "))
e = int(input("ingrese numero: "))
f = int(input("ingrese numero: "))

ecuacion1 = [a,b,c]
ecuacion2 = [d,e,f]


X = (c - b * f / e) / (a - b * d / e)
Y = (f - d * X) / e

print("x=",X , "y=",Y)

      