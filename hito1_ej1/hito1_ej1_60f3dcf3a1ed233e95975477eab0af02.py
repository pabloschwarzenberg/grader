#Nota final
PT = float(input("nota de tareas: "))
PI = float(input("nata de interrogaciones: "))
NE= float(input("nota de examen: "))
PP = float(input("nota de presentacion: "))

PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print ("tu promedio final es", round (PF,1))