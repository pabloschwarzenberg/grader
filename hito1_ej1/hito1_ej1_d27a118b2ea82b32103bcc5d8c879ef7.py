def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

# Solicitar las notas al usuario
nota_pt = float(input("Ingrese la nota de las Tareas (PT): "))
nota_pi = float(input("Ingrese la nota de las Interrogaciones (PI): "))
nota_ne = float(input("Ingrese la nota del Examen (NE): "))
nota_pp = float(input("Ingrese la nota de la Presentación (PP): "))

# Calcular el promedio final
promedio = calcular_promedio_final(nota_pt, nota_pi, nota_ne, nota_pp)

# Imprimir el resultado
print("El promedio final es:", promedio)
      