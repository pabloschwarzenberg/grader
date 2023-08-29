#Nota final
#Recopilacion de datos
PTAREA = float(input("Ingrese las notas de las tareas: "))
PINTERROGACION = float(input("Ingrese las notas de las interrogaciones: "))
NEXAMEN = float(input("Ingrese la nota del examen: "))
PPRESENTACION = float(input("Ingrese las notas de la presentacion: "))

#Calculo de promedio
promedio = 0.3*PTAREA + 0.3*PINTERROGACION + 0.3*NEXAMEN + 0.1*PPRESENTACION

#Imprimir resultado final de promedio
print("El promedio final es:",promedio)