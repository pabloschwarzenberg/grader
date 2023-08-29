#Nota final
Tareas=float(input("Nota de tareas:"))
Interrogaciones=float(input("Nota de interrogaciones:"))
Examen=float(input("Nota de examen:"))
Presentacion=float(input("Nota de presentacion:"))

Promedio_final=(0.3*Tareas)+(0.3*Interrogaciones)+(0.3*Examen)+(0.1*Presentacion)
a=round(Promedio_final,1)
print("Tu promedio final es ", a)

