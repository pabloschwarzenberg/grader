#Nota final

print("Promedio nota final")

PT = float(input("Por favor ingrese el promedio de sus notas correspondientes a 'Tareas': "))
PI = float(input("Por favor ingrese el promedio de sus notas correspondientes a 'Interrogaciones': "))
NE = float(input("Por favor ingrese su nota 'Examen': "))
PP = float(input("Por favor ingrese su nota correspondiente a 'Presentación': "))

#Formula promedio.

Prom_final = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
Prom_final = round(Prom_final,1)

print("La nota correspondiente a su promedio final es: ", Prom_final)

print("Fin.")