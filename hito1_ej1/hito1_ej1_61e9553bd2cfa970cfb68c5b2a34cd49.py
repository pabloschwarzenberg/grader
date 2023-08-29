#Nota final
PT=float(input("Ingrese el promedio de notas en tareas:"))
PI=float(input("Ingrese el promedio de notas en interrogaciones:"))
NE=float(input("Ingrese la nota del examen:"))
PP=float(input("Ingrese el promedio de presentación:"))
Promedio=(((PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1))/4)
print(f"Su promedio es:{Promedio}\n")