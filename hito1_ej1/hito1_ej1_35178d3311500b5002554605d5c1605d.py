#Nota final
PT = float(input("Ingrese su nota de tareas"))
PI = float(input("Ingrese su nota de interragaciones"))
NE = float(input("Ingrese su nota de examen"))
PP = float(input("Ingrese su nota de presentacion"))

PF = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP,1)
print(PF)