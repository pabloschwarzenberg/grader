#Nota final
PT = float(input("ingresa la nota de tarea: "))
PI = float(input("ingresa la nota de interrogantes: "))
NE = float(input("ingresa la nota de examen: "))
PP = float(input("ingresa la nota de presentacion: "))

re= ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))

print("El promedio de las 4 notas es:", round(re,1))
      