def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Solicitar las notas al usuario
nota_pt = float(input("Ingresa la nota de las Tareas (PT): "))
nota_pi = float(input("Ingresa la nota de las Interrogaciones (PI): "))
nota_ne = float(input("Ingresa la nota del Examen (NE): "))
nota_pp = float(input("Ingresa la nota de la Presentacion (PP): "))

# Calcular el promedio final y redondearlo a un decimal
promedio_final = calcular_promedio_final(nota_pt, nota_pi, nota_ne, nota_pp)
print("El promedio final es:", promedio_final)
      