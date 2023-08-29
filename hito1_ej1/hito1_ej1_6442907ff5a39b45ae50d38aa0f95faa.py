      
      def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_redondeado = round(promedio, 1)
    return promedio_redondeado

pt = float(input("Ingrese la nota de las Tareas: "))
pi = float(input("Ingrese la nota de las Interrogaciones: "))
ne = float(input("Ingrese la nota del Examen: "))
pp = float(input("Ingrese la nota de la Presentacion: "))
promedio_final = calcular_promedio_final(pt, pi, ne, pp)
print("El promedio final es:", promedio_final)