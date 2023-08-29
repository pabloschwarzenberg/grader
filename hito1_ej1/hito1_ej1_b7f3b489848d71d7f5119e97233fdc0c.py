#Calculo de Notas

print("Calcula tu promedio final")

print("--------")

PT = float(input("Ingrese tu nota de tareas"))
PI = float(input("Ingrese su nota de Interrogaciones"))
NE = float(input("Ingrese su nota de Examen"))
PP = float(input("Ingrese su nota de Presentacion"))
media= 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print("La nota final del curso es : " , round( media ,1))
 