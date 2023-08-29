#Nota final
pt=float(input("ingrese nota de tarea"))
pi=float(input("ingrese nota interrogacion"))
ne=float(input("ingrese nota examen"))
pp=float(input("ingrese nota de presentacion"))

promedio=0.3*(pt) + 0.3*(pi) + 0.3*(ne) + 0.1*(pp)
print(round(promedio,1))      