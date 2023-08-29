#Nota final

#PT = 0,3
#PI = 0,3
#NE = 0,3
#PP = 0,1


PT = float(input("Ingrese la nota de Tarea: "))

PI = float(input("Ingrese la nota de Interrogaciones: "))

NE = float(input("Ingrese la nota de examen: "))

PP = float(input("Ingrese la nota de presentacion: "))

promedio = PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1

promedioRedondeado = round(promedio, 1)

print(promedioRedondeado)












