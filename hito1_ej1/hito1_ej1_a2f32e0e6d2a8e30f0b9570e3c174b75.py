#Nota final
PT=(float(input("ingrese la nota de sus tareas: ")))
PI=(float(input("ingrese la nota de sus interrogaciones: ")))
NE=(float(input("ingrese la nota de su examen: ")))
PP=(float(input("ingrese la nota de su presentacion: ")))
PF=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)%4
round(PF,1)
print("su promedio es", PF)