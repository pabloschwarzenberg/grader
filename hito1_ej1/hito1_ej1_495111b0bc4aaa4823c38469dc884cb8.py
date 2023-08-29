#Nota final
PT=float(input("Ingresar nota de tareas: "))
PI=float(input("Ingresar nota de interrogaciones: "))
NE=float(input("Ingresar nota de examen: "))
PP=float(input("Ingresar nota de presentación: "))
PF=(PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1)
print("Su promedio final es:",round(PF,1))      