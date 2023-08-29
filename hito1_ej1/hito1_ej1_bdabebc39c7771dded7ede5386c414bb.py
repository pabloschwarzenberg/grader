def calcular_promedio_final():
    pt = float(input("Ingrese la nota de las Tareas: "))
    pi = float(input("Ingrese la nota de las Interrogaciones: "))
    ne = float(input("Ingrese la nota del Examen: "))
    pp = float(input("Ingrese la nota de la Presentacion: "))

    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_final = round(promedio_final, 1)

    print("El promedio final es:", promedio_final)

calcular_promedio_final()
