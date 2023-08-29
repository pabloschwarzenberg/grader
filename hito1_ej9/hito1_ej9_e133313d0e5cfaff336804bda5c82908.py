#Sistema de Ecuaciones
a=float(input("ingrese el primer número real: "))
b=float(input("ingrese el segundo número real: "))
c=float(input("ingrese el tercer número real: "))
d=float(input("ingrese el cuarto número real: "))
e=float(input("ingrese el quinto número real: "))
f=float(input("ingrese el sexto número real: "))
y=(f*a-d*c)/(a*e-d*b)
x=(c-b*y)/a

print("y= ",round(y,1))
print("x= ",round(x,1))