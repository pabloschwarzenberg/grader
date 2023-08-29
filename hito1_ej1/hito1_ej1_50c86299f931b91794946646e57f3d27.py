#programa para calcular las notas

PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota de examen: "))
PP = float(input("Ingrese la nota de presentacion: "))

formula = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
X = round(formula,1) 

print("Sus resultados son: ", X)
 