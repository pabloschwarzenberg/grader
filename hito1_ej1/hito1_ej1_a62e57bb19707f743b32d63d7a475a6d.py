#Programa que calcula el promedio

PT = float(input("Nota Tareas:  "))

PI = float(input("Nota Interrogación:  "))

NE = float(input("Nota Examen:  "))

PP = float(input("Nota Presentacion:  "))

PROMEDIO = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))

round(PROMEDIO,1)

print(PROMEDIO)
