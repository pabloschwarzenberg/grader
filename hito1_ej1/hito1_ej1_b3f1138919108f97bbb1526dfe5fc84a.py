#Nota final
PT = float(input("ingrese la nota de Tareas"))
PI = float(input("ingrese la nota de Interrogaciones"))
NE = float(input("ingrese la nota de Examen"))
PP = float(input("ingrese la nota de Presentacion"))
resp = round(0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP, 1)
print("el promedio final es: ", resp)