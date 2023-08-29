#Sistema de Ecuaciones
a = int(input("ingrese numero: "))
b = int(input("ingrese numero: "))
c = int(input("ingrese numero: "))
d = int(input("ingrese numero: "))
e = int(input("ingrese numero: "))
f = int(input("ingrese numero: "))
determinante = (a*e) - (b*d)
determinante != 0
x = (c*e - b*f)/determinante
y = (a*f - c*d)/determinante
        
print("x=" + str(x))
print("y=" + str(y))
   


