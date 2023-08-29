#Nota final
# Pedir al usuario que ingrese las cuatro notas
PT = float(input("Ingrese la nota de las Tareas (PT): "))
PI = float(input("Ingrese la nota de las Interrogaciones (PI): "))
NE = float(input("Ingrese la nota del Examen (NE): "))
PP = float(input("Ingrese la nota de la Presentación (PP): "))

# Calcular el promedio final utilizando la fórmula
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", round(promedio, 1))
      