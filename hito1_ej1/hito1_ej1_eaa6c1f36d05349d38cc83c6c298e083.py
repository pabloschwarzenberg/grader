def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_final_redondeado = round(promedio_final, 1)
    return promedio_final_redondeado


# Solicitar al usuario ingresar las notas
nota_pt = float(input("Ingrese la nota de Tareas: "))
nota_pi = float(input("Ingrese la nota de Interrogaciones: "))
nota_ne = float(input("Ingrese la nota de Examen: "))
nota_pp = float(input("Ingrese la nota de Presentacion: "))

# Calcular el promedio final y redondearlo a un decimal
promedio_final = calcular_promedio_final(nota_pt, nota_pi, nota_ne, nota_pp)

# Imprimir el resultado
print("El promedio final es:", promedio_final)
