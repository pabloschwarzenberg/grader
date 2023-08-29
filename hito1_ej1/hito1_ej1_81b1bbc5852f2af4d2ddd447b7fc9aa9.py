#Nota final
PT=float(input("Ingrese la nota de tareas:"))
PI=float(input("Ingrese la nota de interrogantes:"))
NE=float(input("Ingrese la nota de Examen:"))
PP=float(input("Ingrese la nota de presentacion:"))
PF=((PT*3/10)+(PI*3/10))+(NE*3/10)+(PP*1/10)
PF=round(PF,1)
print("El promedio final es:",PF)