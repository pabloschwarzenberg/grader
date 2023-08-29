def calcular_la_nota_final(pt, pi, ne, pp):
    nota = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(nota, 1)

pt = float(input("Ingresa tu nota de las Tareas (PT): "))
pi = float(input("Ingresa tu nota de las Interrogaciones (PI): "))
ne = float(input("Ingresa tu nota del Examen (NE): "))
pp = float(input("Ingresa tu nota de la Presentacion (PP): "))

nota_final = calcular_la_nota_final(pt, pi, ne, pp)
print("La nota final es: " + str(nota_final))