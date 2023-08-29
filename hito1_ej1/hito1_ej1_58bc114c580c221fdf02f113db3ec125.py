#Nota final
X = float(input("ingrese la nota de la tarea:"))
Y = float(input("ingrese la nota de la interrogacion:"))
Z = float(input("ingrese la nota del examen:"))
W = float(input("ingrese la nota de la presentacion:"))
promedio = round((0.3*X + 0.3*Y + 0.3*Z + 0.1*W)**1,1)
print(promedio)      