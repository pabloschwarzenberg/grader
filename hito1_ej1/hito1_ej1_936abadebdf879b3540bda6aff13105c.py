#Nota final
PT = eval(input('Ingrese la nota de las tareas: '))
PI = eval(input('Ingrese la nota de las interrogaciones: '))
NE = eval(input('Ingrese la nota del examen: '))
PP = eval(input('Ingrese la nota de presentación: '))
NF = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
n = round(NF*10)
print(n/10)