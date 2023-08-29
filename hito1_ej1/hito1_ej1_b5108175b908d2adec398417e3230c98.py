#Nota final
PT = float(input("Ingrese su nota de tareas", ))
PI = float(input("ingrese su nota de interrogaciones", ))
NE = float(input("Ingrese  su nota de examen", ))
PP = float(input("ingrese su nota de presentacion", ))
NF = (0.3 * PT) + (0.3 * PI) + (0.1 * PP) + (0.3 * NE)
print("Su nota final es", (round(NF, 1)))
