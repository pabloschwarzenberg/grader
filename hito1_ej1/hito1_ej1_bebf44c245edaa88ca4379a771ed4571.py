#Nota final
PT=(float(input("Nota de tareas: ")))
PI=(float(input("Nota de interrogaciones: ")))
NE=(float(input("Nota de examen: ")))
PP=(float(input("Nota de presentacion: ")))
NF=(3*PT+3*PI+3*NE+1*PP)/10
print(round(NF,1))