"""
3.- Realiza un programa para preguntar al usuario cuatro notas:
•	PT = Tareas
•	PI = Interrogaciones
•	NE= Examen
•	PP = Presentacion
Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
Imprime el resultado redondeado a un decimal.
"""
PT = float(input("Tareas: "))
PI = float(input("Interrogaciones: "))
NE = float(input("Exámen: "))
PP = float(input("Presentación: "))

promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(promedio_final)
      