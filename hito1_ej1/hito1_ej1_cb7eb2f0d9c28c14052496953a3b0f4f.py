#Nota final
PT=float(input("ingrese la nota de la tarea:"))
PI=float(input("ingrese la nota de la interrogración:"))
NE=float(input("ingrese la nota del examen:"))
PP=float(input("iingrese la nota de la presentación:"))
promedio=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
promedio=round(promedio,1)
print("el promedio final es:",promedio)