# Realiza un programa para preguntar al usuario cuatro notas:

# PT = Tareas
# PI = Interrogaciones
# NE= Examen
# PP = Presentacion
# Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
# Imprime el resultado redondeado a un decimal.

# Nota final
pt = float(input("Ingresa nota de tareas: "))
pi = float(input("Ingresa nota de interrogaciones: "))
ne = float(input("Ingresa nota de examen: "))
pp = float(input("Ingresa nota de presentación: "))
promedio = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
promedio_redondeado = round(promedio, 1)
print(promedio_redondeado)
