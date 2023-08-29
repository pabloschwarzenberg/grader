#Nota final
PT=float(input("Ingrese su nota por tareas"))
PI=float(input("Ingrese su nota por Interrogaciones"))
NE=float(input("Ingrese su nota por Examen"))
PP=float(input("Ingrese su nota por Presentacion"))
print (round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP, 1))