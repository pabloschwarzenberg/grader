pt= float(input(" Ingrese nota de tarea:\n "))
pi= float(input(" Ingrese nota de interrogacion:\n "))
ne= float(input(" Ingrese nota de examen:\n "))
pp= float(input(" Ingrese nota de presentacion:\n "))

promedio = ((0.1 * pp) + (0.3 * pi) + (0.3 * ne) + (pt * 0.3))
print("Tu promedio final es:", round(promedio,1))      