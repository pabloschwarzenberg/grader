from os import system
system ("cls")
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    promedio_final = round(promedio_final, 1)
    print("El promedio final es:", promedio_final)

# Solicitar las notas al usuario
PT = float(input("Ingrese la nota de Tareas (PT): "))
PI = float(input("Ingrese la nota de Interrogaciones (PI): "))
NE = float(input("Ingrese la nota de Examen (NE): "))
PP = float(input("Ingrese la nota de Presentación (PP): "))

# Calcular el promedio final y imprimir el resultado
calcular_promedio_final(PT, PI, NE, PP)
  