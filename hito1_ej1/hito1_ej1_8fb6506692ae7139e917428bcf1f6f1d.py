def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Solicitar las notas al usuario
nota_pt = float(input("Ingrese la nota de PT: "))
nota_pi = float(input("Ingrese la nota de PI: "))
nota_ne = float(input("Ingrese la nota de NE: "))
nota_pp = float(input("Ingrese la nota de PP: "))

# Llamar a la función y mostrar el resultado
resultado = calcular_promedio_final(nota_pt, nota_pi, nota_ne, nota_pp)
print("El promedio final es:", resultado)
