#Nota final
#Entrada:
pt = float(input("Ingresa tu nota de tarea: "))
pi = float(input("Ingresa tu nota de interrogaciones: "))
ne = float(input("Ingresa tu nota de examen: "))
pp = float(input("Ingresa tu nota de presentación: "))

#Procedimiento:

notaF = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
notaFredo = round(notaF,1)

#Salida:
print("Tu nota final es:", notaFredo)
      