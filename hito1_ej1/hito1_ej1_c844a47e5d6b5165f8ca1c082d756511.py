import math

PT=input("Ingrese su nota de promedio de tareas: ")
PI=input("Ingrese su nota de promedio de interrogaciones: ")
NE=input("Ingrese su nota del examen: ")
PP=input("Ingrese su nota de promedio de presentaciones: ")
PF=round(float(0.3*(float(PT)) + 0.3*(float(PI)) + 0.3*(float(NE)) + 0.1*(float(PP))),1)

print("Su promedio es: ", PF)