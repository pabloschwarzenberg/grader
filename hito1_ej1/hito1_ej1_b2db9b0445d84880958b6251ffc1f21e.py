PT = float(input("Ingrese su nota de tarea: "))
PI = float(input("Ingrese su nota de interrogaciones: "))
NE = float(input("Ingrese su nota de examen: ")) 
PP = float(input("Ingrese su nota de presentación: "))
NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Su promedio final de notas es", round(NF,1))