#Nota final
PT = eval(input("Ingrese nota de Tareas\n"))
PI = eval(input("Ingrese nota de Interrogaciones\n"))
NE = eval(input("Ingrese nota de Examen\n"))
PP = eval(input("Ingrese nota de Presentación\n"))
pf = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El promedio final es de: ",round(pf,1))      