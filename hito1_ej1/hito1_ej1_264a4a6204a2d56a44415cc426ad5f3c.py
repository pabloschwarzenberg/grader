#Nota fina
PT = eval(input("Por favor, ingrese la nota de las tareas: "))
PI = eval(input("Por favor, ingrese la nota de las interrogaciones: "))
NE = eval(input("Por favor, ingrese la nota de los examenes: "))
PP = eval(input("Por favor, ingrese la nota de las presentaciones: "))

PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print(round(PF, 1))