#Algoritmo que calcula promedio de notas de acuerdo a una ponderación.

#Solicita el ingreso de notas.
nota_tareas = float(input("Ingrese promedio de tareas : "))
nota_interrogaciones = float(input("Ingrese promedio de interrogaciones : "))
nota_examen = float(input("Ingrese nota de examen : "))
nota_presentacion = float(input("Ingrese promedio de presentacion : "))

#Calcula promedio aplicando ponderación.
promedio_final = (nota_tareas * 0.3) + (nota_interrogaciones* 0.3) + (nota_examen* 0.3) + (nota_presentacion * 0.1) 

#Imprime resultado.
print(  round(promedio_final , 1)  )