#Sistema de Ecuaciones
num1 = float(input("Ingrese primer número: "))
num2 = float(input("Ingrese segundo número: "))
num3 = float(input("Ingrese tercer número: "))
num4 = float(input("Ingrese cuarto número: "))
num5 = float(input("Ingrese quinto número: "))
num6 = float(input("Ingrese sexto número: "))

"""
Metodo Regla de Cramer 

"""

m1 = (num1*num5)-(num2*num4)
mx = (num3*num5)-(num6*num2)
my = (num1*num6)-(num4*num3)
x = mx/m1
y = my/m1

redonx = round(x,1)
redony = round(y,1)

print("x=", redonx, "y=", redony)      