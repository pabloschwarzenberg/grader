def calcular_nota_final(pt, pi, ne, pp):
    nota_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(nota_final, 1)

# Solicitar las notas al usuario
pt = float(input("Ingrese la nota de las Tareas (PT): "))
pi = float(input("Ingrese la nota de las Interrogaciones (PI): "))
ne = float(input("Ingrese la nota del Examen (NE): "))
pp = float(input("Ingrese la nota de la Presentación (PP): "))

# Calcular la nota final
nota_promedio = calcular_nota_final(pt, pi, ne, pp)

# Imprimir el resultado
print("La nota final promedio es:", nota_promedio)