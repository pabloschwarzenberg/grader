#Nota final
PT=float(input("ingrese la nota de Tareas:"))
PI=float(input("ingrese la nota de interrogaciones:"))
NE=float(input("ingrese la nota del examen:"))
PP=float(input("ingrese la nota de presentacion:"))

prom = ((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))
print("el resultado final es: %.1f" %prom)