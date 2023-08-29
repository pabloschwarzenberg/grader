#Sistema de Ecuaciones

#Escribe un programa que resuelva un sistema de dos ecuaciones con dos incognitas. 
#Tu programa recibirá los seis números reales que representan el sistema y deberá imprimir la dos soluciones redondeadas a un decimal. Ejemplo: Para el sistema 2x+3y=6 y x+2y=5, tu programa debe imprimir

#x=-3.0
#y=4.0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

# A + B = C
# D + E = F

delta = (a * e) - (d * b)

delta_x = (c * e) - (f * b)
delta_y = (a * f) - (d * c)

x = delta_x / delta
y = delta_y / delta

print("x=" + str(x))
print("y=" + str(y))