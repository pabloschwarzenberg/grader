def calcular_promedio_final(pt, pi, ne, pp):
    # Calcula el promedio final utilizando la fórmula dada
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)  # Redondea el promedio a un decimal

# Solicita al usuario que ingrese las cuatro notas
notas = []
notas.append(float(input("Ingrese la nota de las Tareas: ")))
notas.append(float(input("Ingrese la nota de las Interrogaciones: ")))
notas.append(float(input("Ingrese la nota del Examen: ")))
notas.append(float(input("Ingrese la nota de la Presentación: ")))

# Desempaqueta las notas y calcula el promedio final llamando a la función calcular_promedio_final
promedio_final = calcular_promedio_final(*notas)

# Imprime el promedio final redondeado a un decimal
print("El promedio final es:", promedio_final)

      