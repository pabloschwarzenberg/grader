#Nota final
PT=float(input("Ingrese la nota final de las Tareas:"))
PI=float(input("Ingrese la nota final de las Interrogaciones:"))
NE=float(input("Ingrese la nota final de los exámenes:"))
PP=float(input("Ingrese la nota final de las presentaciones:"))
pf=(PT*0.3+PI*0.3+NE*0.3+PP*0.1)
print(round(pf,1))