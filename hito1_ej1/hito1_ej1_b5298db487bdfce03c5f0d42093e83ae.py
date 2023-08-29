#Nota final
PT = eval(input("Ingrese la nota de Tareas: "))
PI = eval(input("Ingrese la nota de Interrogaciones: "))
NE = eval(input("Ingrese la nota de Examenes: "))
PP = eval(input("Ingrese la nota de Presentacion: "))

NF = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
NR = (round(NF, 1))
print(NR)