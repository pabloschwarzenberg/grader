#Nota final
T = float(input("ingrese la nota de la tarea:"))
I = float(input("ingrese la nota de la interrogacion:"))
E = float(input("ingrese la nota del examen:"))
P = float(input("ingrese la nota de la presentacion:"))
promedio=round((0.3*T + 0.3*I + 0.3*E + 0.1*P)**1,1)
print(promedio)