#Sistema de Ecuaciones
x1 = int(input("ingresa el x: "))
y1 = int(input("ingresa el y: "))
n1 = int(input("ingresa el n1: "))
x2 = int(input("ingresa el x2: "))
y2 = int(input("ingresa el y2: "))
n2 = int(input("ingresa el n2: "))

a = (n2*x1)-(x2*n1)
b = (x1*y2)-(x2*y1)
r2 = a/b

c = n1-y1*r2
d = x1
r1 = c/d

r2 = round(r2,1)
r1 = round(r1,1)

print('x=',r1)
print('y=', r2)