PT = float(input("Indique la calificación de tareas: "))
PI = float(input("Indique la calificación de interrogaciones: "))
NE = float(input("Indique la calificación de exámen: "))
PP = float(input("Indique la calificación de presentación: "))

NoFi = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

print("Nota Final:",round(NoFi,1))