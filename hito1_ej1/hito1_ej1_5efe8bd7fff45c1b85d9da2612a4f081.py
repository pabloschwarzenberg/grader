#Ingrese los valores respectivos
pt= float(input(" Ingrese la nota de la tarea:\n "))
pi= float(input(" Ingrese la nota de la interrogacion:\n "))
ne= float(input(" Ingrese la nota del examen:\n "))
pp= float(input(" Ingrese la nota de la presentacion:\n "))

promedio = ((0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (pp * 0.1))

print("El promedio final es:", round(promedio,1))      