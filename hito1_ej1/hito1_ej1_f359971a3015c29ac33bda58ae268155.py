PT=float(input("Ingrese la nota final de tareas: "))
PI=float(input("Ingrese la nota de interrogaciones: "))
NE=float(input("Ingrese la nota del examen: "))
PP=float(input("Ingrese la nota de presentacion: "))
NF=(PT*0.3)+(PI*0.3)+(NE * 0.3)+(PP*0.1)

print(round(NF,1))
