#Hito 1 > Nota Final
#Realiza un programa para preguntar al usuario cuatro notas:
#PT = Tareas #PI = Interrogaciones #NE= Examen #PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprime el resultado redondeado a un decimal.

PT = float(input("Ingrese la nota obtenida de las tareas.........: "))
PI = float(input("Ingrese la nota obtenida de las interrogaciones: "))
NE = float(input("Ingrese la nota obtenida del exámen............: "))
PP = float(input("Ingrese la nota obtenida de la presentación....: "))
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("La nota final es: " + str(round(promedio,1)))