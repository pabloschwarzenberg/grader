#Nota final
PT=eval(input("ingrese la nota de tareas"))
PI=eval(input("ingrese la nota de interrogaciones"))
NE=eval(input("ingrese la nota de examen"))
PP=eval(input("ingrese la nota de presentacion"))
PF=0.3*PT+0.3*PI+0.3*NE+0.1*PP
pf=round(PF,1)
print(pf)