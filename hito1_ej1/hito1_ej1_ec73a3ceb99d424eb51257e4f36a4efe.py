# Nota final
PT = eval(input("Ingrese la nota de la tarea"))
PI = eval(input("Ingrese la nota de la interrogacion"))
NE = eval(input("Ingrese la nota del examen"))
PP = eval(input("Ingrese la nota de la presentacion"))

promedio_final = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print(round(promedio_final,1))