def calcular_promedio_final(PT, PI, NE, PP):
  promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
  return round(promedio, 1)

PT = float(input("Ingresa la nota de Tareas (PT): "))
PI = float(input("Ingresa la nota de Interrogaciones (PI): "))
NE = float(input("Ingresa la nota de Examen (NE): "))
PP = float(input("Ingresa la nota de Presentación (PP): "))

promedio_final = calcular_promedio_final(PT, PI, NE, PP)

print("El promedio final es:", promedio_final)
