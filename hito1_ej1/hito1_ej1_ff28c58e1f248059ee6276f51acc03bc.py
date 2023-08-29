#Nota final
PT = float(input("ingrese su nota de tareas : "))
PI = float(input("ingrese su nota de interrogaciones : "))
NE = float(input("ingrese su nota del examen : "))
PP = float(input("ingrese su nota de presentacion : "))

PF = ((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP))

print("su promedio final es : " , round(PF,1))
