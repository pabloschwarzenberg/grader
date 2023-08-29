#Nota final
#Entrada
PT = input("Ingrese su nota de tareas: ")
PT = float(PT)
PI = input("Ingrese su nota de interrogaciones: ")
PI = float(PI)
NE = input("Ingrese su nota de examen: ")
NE = float(NE)
PP = input("Ingrese su nota de presentacion: ")
PP = float(PP)

Promedio_final = float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print(round(Promedio_final, 1))
