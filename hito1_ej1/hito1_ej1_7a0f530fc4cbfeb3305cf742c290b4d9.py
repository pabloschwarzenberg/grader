pt= float(input(" Ingrese nota de tarea:\n "))
pi= float(input(" Ingrese nota de interrogacion:\n "))
ne= float(input(" Ingrese nota de examen:\n "))
pp= float(input(" Ingrese nota de presentacion:\n "))

promedio = ((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (pp * 0.1))

print("El promedio final es:", round(promedio,1))

      