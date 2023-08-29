#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese rut sin digito verificador: "))

#Descomponer numero
a = (rut//10000000)%10
b = (rut//1000000)%10
c = (rut//100000)%10
d = (rut//10000)%10
e = (rut//1000)%10
f = (rut//100)%10
g = (rut//10)%10
h = (rut//1)%10

#Operaciones
a1 = a*3
b1 = b*2
c1 = c*7
d1 = d*6
e1 = e*5
f1 = f*4
g1 = g*3
h1 = h*2

p = a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1
z = p//11
r = p-(11*z)
y = 11 - r

#Condicionales
if y == 11:
    print("dv=0")
if y == 10:
    print("dv=K")
if y != 11 and y != 10:
    print("dv=",y)      