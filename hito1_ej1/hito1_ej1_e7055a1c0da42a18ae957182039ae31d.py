#Nota final
def calculate_final_grade(pt, pi, ne, pp):
    final_grade = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(final_grade, 1)

# Solicitar las notas al usuario
pt = float(input("Ingrese la nota de las Tareas: "))
pi = float(input("Ingrese la nota de las Interrogaciones: "))
ne = float(input("Ingrese la nota del Examen: "))
pp = float(input("Ingrese la nota de la Presentacion: "))

# Calcular el promedio final
result = calculate_final_grade(pt, pi, ne, pp)

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", result)
      