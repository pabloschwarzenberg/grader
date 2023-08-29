def promediofinal():
    pt = float(input("Ingresa la nota de Tareas (PT): "))
    pi = float(input("Ingresa la nota de Interrogaciones (PI): "))
    ne = float(input("Ingresa la nota de Examen (NE): "))
    pp = float(input("Ingresa la nota de Presentación (PP): "))

    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_final_redondeado = round(promedio_final, 1)

    print("El promedio final es:", promedio_final_redondeado)

promediofinal()
