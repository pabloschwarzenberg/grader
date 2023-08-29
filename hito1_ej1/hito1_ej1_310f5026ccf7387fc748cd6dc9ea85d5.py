#Realiza un programa para preguntar al usuario cuatro notas:

#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprime el resultado redondeado a un decimal.

PT = float(input("ingrese la nota de sus tareas:"))
PI = float(input("ingrese la nota de sus interrogaciones:"))
NE = float(input("ingrese la nota de sus examenes:"))
PP = float(input("ingrese la nota de sus presentaciones:"))

nf = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))

print("tu nota final es:",nf)

