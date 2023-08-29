#Nota final
PT=float(input("ingrese nota de tareas:"))
PI=float(input("ingrese nota de interrogacion:" ))
NE=float(input("ingrese nota de examen:"))
PP=float(input("ingrese nota presentacion:"))

Final=0.3*PT+0.3*PI+0.3*NE+0.1*PP
print(round(Final,1))   