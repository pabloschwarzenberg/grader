#Sistema de Ecuaciones
   
a = float(input("ingresa un numero para A:"))

b = float(input("ingresa un numero para B:"))

c = float(input("ingresa un numero para C:"))

a2 = float(input("ingresa un numero para A2:"))

b2 = float(input("ingresa un numero para B2:"))

c2 = float(input("ingresa un numero para C2:"))

#Procesamiento

x = (c * b2 - b * c2) // (a * b2 - b * a2)

y = (a * c2 - c * a2) // (a * b2 - b * a2)

print("x =", x)

print("y =", y)