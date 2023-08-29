#Nota final
PT=float(input("ingrese promedio de tareas"))
PI=float(input("ingrese promedio de interrogaciones"))
NE=float(input("ingrese nota examen"))
PP=float(input("ingrese el promedio de presentacion al examen"))
a=0.3*PT
b=0.3*PI
c=0.3*NE
d=0.1*PP
promedio_final=a+b+c+d
print(round(promedio_final,1))