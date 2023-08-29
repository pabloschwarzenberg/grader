#Nota final
pt = float(input("ingrese nota de tarea:\n"))
pi = float(input("ingrese nota de interrogacion:\n"))
ne =float(input("ingrese nota de examen:\n"))
pp =float(input("ingrese nota de presentacion:\n"))

promedio = ((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (pp *0.1))

print("el promedio final es:", round(promedio,1))
