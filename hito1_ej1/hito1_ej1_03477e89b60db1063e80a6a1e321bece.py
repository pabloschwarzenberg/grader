#Nota final
promedio_tareas = float(input("Ingrese su nota de promedio de tareas: "))
promedio_interrogaciones = float(input("Ingrese su nota de promedio de interrogaciones: "))
nota_examen = float(input("Ingrese su nota de examen: "))
presentacion = float(input("Ingrese su nota de presentacion: "))
promedio_final = round(0.3*(promedio_tareas) + 0.3*(promedio_interrogaciones) + 0.3*(nota_examen) + 0.1*(presentacion),1)
print(promedio_final)