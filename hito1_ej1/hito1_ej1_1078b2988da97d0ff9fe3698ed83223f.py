#Nota final


PT = float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE = float(input("Ingrese nota de examen: "))
PP = float(input("Ingrese nota de presentacion: "))

notafinal = round((PT*0.3 + PI* 0.3 + NE*0.3 + PP *0.1),1)

print(notafinal)