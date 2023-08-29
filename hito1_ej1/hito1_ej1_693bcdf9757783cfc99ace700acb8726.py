#Nota final
print("promedio")
PT= float(input("Tareas: "))
PI= float(input("Interrogaciones: "))
NE= float(input("Examen: "))
PP= float(input("Presentacion"))

promedio= (PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1) 
promedio_redondeado= round(promedio, 1)

print ("el promedio es: ", promedio_redondeado)
