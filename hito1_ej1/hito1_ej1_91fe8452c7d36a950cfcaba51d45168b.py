#Nota final
t=float(input("ingrese la nota de la tarea:"))
i=float(input("ingrese la nota de la interrogacion:"))
e=float(input("ingrese la nota del examen:"))
p=float(input("ingrese la nota de la presentacion:"))
promedio=round((0.3*t+0.3*i+0.3*e+0.1*p)**1,1)
print(promedio)    