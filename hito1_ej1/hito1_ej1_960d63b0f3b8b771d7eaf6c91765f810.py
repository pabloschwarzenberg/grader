def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_redondeado = round(promedio, 1)
    return promedio_redondeado

# Ejemplo de uso
nota_pt = float(input("Ingresa la nota de las Tareas: "))
nota_pi = float(input("Ingresa la nota de las Interrogaciones: "))
nota_ne = float(input("Ingresa la nota del Examen: "))
nota_pp = float(input("Ingresa la nota de la Presentación: "))

promedio_final = calcular_promedio_final(nota_pt, nota_pi, nota_ne, nota_pp)
print("El promedio final es:", promedio_final)
