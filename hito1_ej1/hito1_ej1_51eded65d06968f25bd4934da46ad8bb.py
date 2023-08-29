Interrogaciones=float(input('Ingrese nota de Interrogaciones: '))
Examen=float(input('Ingrese nota de Examen: '))
Tareas=float(input('Ingrese nota de tareas: '))
Presentacion=float(input('Ingrese nota de Presentacion: '))

nota_final=((Interrogaciones*0.3)+(Examen*0.3)+(Tareas*0.3)+(Presentacion*0.1))
print (round(nota_final,1))
print(Interrogaciones,Examen,Presentacion,Tareas)