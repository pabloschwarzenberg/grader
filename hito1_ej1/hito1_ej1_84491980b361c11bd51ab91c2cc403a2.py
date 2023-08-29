#Nota final
PT=float(input("Ingrese la nota de las tareas:"))
PI=float(input("Ingrese la nota de interrogacion:"))
NE=float(input("Ingrese la nota de examen:"))
PP=float(input("Ingrese la nota de presentacion:"))
Promedio=(0.3*PT+0.3*PI+0.3*NE+0.1*PP)
PF=round(Promedio,1)
print("su promedio final es",PF)