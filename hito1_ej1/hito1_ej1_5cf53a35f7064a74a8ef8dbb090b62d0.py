#Nota final
PT = eval(input("ingrese la nota de las tareas "))
PI = eval(input("ingrese la nota de las interrogaciones "))
NE = eval(input("ingrese la nota de el examen "))
PP = eval(input("ingrese la nota de la presentacion "))
PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
PF = round(PF, 1)
print(PF)