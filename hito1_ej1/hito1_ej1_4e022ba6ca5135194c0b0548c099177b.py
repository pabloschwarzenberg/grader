#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_final_redondeado = round(promedio_final, 1)
    print("El promedio final es:", promedio_final_redondeado)


pt = float(input("Ingrese la nota de Tareas (PT): "))
pi = float(input("Ingrese la nota de Interrogaciones (PI): "))
ne = float(input("Ingrese la nota de Examen (NE): "))
pp = float(input("Ingrese la nota de Presentación (PP): "))


calcular_promedio_final(pt, pi, ne, pp)      