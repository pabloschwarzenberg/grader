#Nota final

print("Ingrese la nota de tareas: ")
PT = float(input())
print("Ingrese la nota de interrogaciones: ")
PI = float(input())
print("Ingrese la nota de examen: ")
NE = float(input())
print("Ingrese la nota de presentación: ")
PP = float(input())

PF = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

print("Su nota final es: ", round(PF,1))