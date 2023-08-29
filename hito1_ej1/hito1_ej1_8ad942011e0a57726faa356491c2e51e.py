PT = float(input("Ingrese Nota en Tareas: "))
PI = float(input("Ingrese Nota de Interrogaciones: "))
NE = float(input("Ingrese Nota de Examen: "))
PP = float(input("Ingrese Nota de Presentación: "))
A = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
A2 = round(A,1)
print ("La nota final es: ", A2)
