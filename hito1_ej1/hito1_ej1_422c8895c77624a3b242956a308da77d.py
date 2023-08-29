#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
  promedio= 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
  promedio_redondeado = round(promedio, 1)
  return promedio_redondeado

PT = float(input("ingrese la nota de tareas: "))
PI = float(input("ingrese la nota de interrogaciones: "))
NE = float(input("ingrese la nota del examen: "))
PP = float(input("ingrese la nota de presentacion: "))

promedio_final = calcular_promedio_final(PT,PI , NE, PP)

print("el promedio final es:", promedio_final)