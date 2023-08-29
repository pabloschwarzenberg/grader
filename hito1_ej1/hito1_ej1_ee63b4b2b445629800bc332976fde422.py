#Nota final
PT = float(input(" Tareas : "))
PI = float(input( " Interrogaciones : "))
NE = float(input(" Examen : "))
PP = float(input(" Presentacion : "))

promedio = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP ) % 4
round( promedio ,1 )
print ("el promedio es ", promedio)