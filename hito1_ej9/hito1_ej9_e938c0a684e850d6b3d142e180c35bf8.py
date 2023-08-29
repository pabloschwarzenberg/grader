#Sistema de Ecuaciones
z1 = int(input("ingrese  z1: "))
j1 = int(input("ingrese  j1: "))
t1 = int(input("ingrese  t1: "))
z2 = int(input("ingrese  z2: "))
j2 = int(input("ingrese  j2: "))
t2 = int(input("ingrese  t2: "))

a = (t2*z1)-(z2*t1)
b = (z1*j2)-(z2*j1)
r2 = a/b

c = t1-j1*r2
d = z1
r1 = c/d

r2 = round(r2,1)
r1 = round(r1,1)

print('x=',r1)
print('y=', r2)      