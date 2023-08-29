#Nota final
print("Ingrese sus calificaciones")
PT = float(input("Primera calificación: "))
PI = float(input("Segunda calificación: "))
NE = float(input("Tercera calificación: "))
PP = float(input("Cuarta calificación: "))
A = 0.3*PT
B = 0.3*PI
C = 0.3*NE
D = 0.1*PP
Promedio = A + B + C + D
print("Su promedio es %.1f" % Promedio)