#Nota final
PT = input(" Ingresar nota tareas: ")
PT = float(PT)
PI = input(" Ingresar nota interrogaciones: ")
PI = float(PI)
NE = input(" Ingresar nota examen: ")
NE = float(NE)
PP = input(" Ingresar nota presentación: ")
PP = float(PP)
Promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(Promedio,1))
      