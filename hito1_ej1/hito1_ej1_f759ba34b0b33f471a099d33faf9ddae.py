pt = input("Introduzca nota de Tareas: ")
pi = input("Introduzca nota de Interrogaciones: ")
ne = input("Introduzca nota de Examen: ")
pp = input("Introduzca nota de Presentación: ")
cantidad_notas = 4
promedio = 0

promedio = ((0.3 * float(pt)) + (0.3 * float(pi)) + (0.3 * float(ne)) + (0.1 * float(pp)))

print("Promedio final: {}".format(round(promedio, 1)))