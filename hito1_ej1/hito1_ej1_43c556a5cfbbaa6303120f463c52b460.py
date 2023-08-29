#Nota final
print("Ingrese las 4 notas del curso para calcular su promedio final:\nPT = Tareas\nPI = Interrogaciones\nNE = Examen\nPP = Presentación\n\n")
PT = float(input("PT = "))
PI = float(input("PI = "))
NE = float(input("NE = "))
PP = float(input("PP = "))

Promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
Aproxpromedio = round(Promedio,1)
print("Tu promedio final es ",Aproxpromedio)
print("Gracias!")
