PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota de examen: "))
PP = float(input("Ingrese la nota de presentacion: "))

TT = (PT*3/10) + (3/10*PI) + (3/10 * NE) + (1/10 * PP)
print(round(TT,1))
