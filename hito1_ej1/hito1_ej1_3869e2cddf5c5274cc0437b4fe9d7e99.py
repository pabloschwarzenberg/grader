#Nota final
pt= float(input("ingrese nota de tarea:\n "))
pi= float(input("ingrese nota de interrogación:\n "))
ne= float(input("ingrese nota de examen:\n "))
pp= float(input("ingrese nota de presentación:\n "))

#se saca el promedio 

promedio = ((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (pp * 0.1))

print("El promedio final es:", round(promedio, 1))
