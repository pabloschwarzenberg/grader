#Entrada de notas
Tareas = float(input("Ingrese su nota de tareas: "))
Interrogaciones = float(input("Ingrese su nota de interrogaciones: "))
Examen = float(input("Ingrese su nota de examen: "))
Presentacion = float(input("Ingrese su nota de presentacion: "))

PT = Tareas
PI = Interrogaciones
NE = Examen
PP = Presentacion

#Calculo del promedio

x = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 2)
print("Promedio final: ", x)
