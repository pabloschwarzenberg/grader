#Nota final
PT = float(input("Ingrese su nota de las tareas: "))
PI = float(input("Ingrese su nota de las interrogaciones: "))
NE = float(input("Ingrese su nota de las examen: "))
PP = float(input("Ingrese su nota de las presentacion: "))

PromedioF = (0.3*PT) + (0,3*PI) + (0.3*NE) + (0.1*PP)

print("Su promedio es: ", round(PromedioF, 2))    