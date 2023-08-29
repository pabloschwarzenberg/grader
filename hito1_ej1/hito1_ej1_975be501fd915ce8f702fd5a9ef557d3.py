#Nota final
PT = float(input("Ingrese Nota de Tareas: "))
PI = float(input("Ingrese nota de Interrogaciones: "))
NE = float(input("Ingrese Nota Examen: "))
PP = float(input("Ingrese nota de Presentación: "))
Promedio_Final= (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("Su promedio final es:",round(Promedio_Final,1))