#Nota final
      #PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprime el resultado redondeado a un decimal.

#Nota final
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentación: "))

promedio = round((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP), 1)

print("El promedio final es:", promedio)