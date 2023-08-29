#Nota final
## ENTRADA DE DATOS - PROCESO - SALIDA DE DATOS

PT = float(input("Ingresa nota de Tareas : "))
PI = float(input("Ingresa nota de Interrogaciones : "))
NE = float(input("Ingresa nota de Examen : "))
PP = float(input("Ingresa nota de Presentación : "))

Promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
Promedio = round(Promedio, 1)

print("El Promedio final es :", Promedio)

      