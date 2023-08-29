#Nota final
PT = float(input("ingrese las notas de sus tareas: "))
PI = float(input("ingrese las notas de sus interrogaciones: "))
NE = float(input("ingrese las notas de su examen: "))
PP = float(input("ingrese las notas de su presentacion: "))
promedio_final = 0.3*(PT)+0.3*(PI)+0.3*(NE)+0.1*(PP)
promedio_redondeado = round(promedio_final,1)
print("su promedio final es", (promedio_redondeado))