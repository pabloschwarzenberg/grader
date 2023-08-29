PI = float(input("ingrese nota de Interrogaciones:"))
NE = float(input("ingrese nota de Examen:"))
PP = float(input("ingrese nota de Presentacion:"))
PT = float(input("ingrese nota de Tareas:"))

Promedio_Final = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

print("Alumno tu promedio es:",round(Promedio_Final,1))
