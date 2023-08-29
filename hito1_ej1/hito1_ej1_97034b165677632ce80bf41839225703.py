def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_redondeado = round(promedio, 1)
    return promedio_redondeado


# Solicitar al usuario que ingrese las cuatro notas
nota_PT = float(input("Ingrese la nota de PT: "))
nota_PI = float(input("Ingrese la nota de PI: "))
nota_NE = float(input("Ingrese la nota de NE: "))
nota_PP = float(input("Ingrese la nota de PP: "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(nota_PT, nota_PI, nota_NE, nota_PP)

# Imprimir el resultado redondeado
print("El promedio final es:", promedio_final)
