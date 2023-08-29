#Nota final
PT=float(input("ingresa la nota de tareas:"))
PI=float(input("ingresa la nota de interrogantes:"))
NE=float(input("ingresa la nota de examen:"))
PP=float(input("ingresa la nota de presentacion:"))
NF=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("su nota es,",round(NF,1),",exito!!")  