PT = eval(input("Ingrese nota total de tareas: "))
PI = eval(input("Ingrese nota total de interrogaciones: "))
NE = eval(input("Ingrese nota de examen: "))
PP = eval(input("Ingrese nota de Presentación: "))

Promedio_final = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
Promedio_final = round(Promedio_final,1)
print(Promedio_final)
      