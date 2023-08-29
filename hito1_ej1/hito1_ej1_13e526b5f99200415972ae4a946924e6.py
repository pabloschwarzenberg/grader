#Nota final
PT = eval(input("ingrese la nota de tareas: "))
PI = eval(input("ingrese la nota de interrogaciones: "))
NE = eval(input("ingrese la nota de examen: "))
PP = eval(input("ingrese la nota de presentaciones: "))

formula = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(formula,1))