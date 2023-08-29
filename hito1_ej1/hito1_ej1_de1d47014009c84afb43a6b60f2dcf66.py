#Nota final
PT = eval(input('Ingrese nota de tareas:'))
PI = eval(input('Ingrese nota de interrogaciones:'))
NE = eval(input('Ingrese nota de examen:'))
PP = eval(input('Ingrese nota de presentacion:'))

PF = (0.3)*PT+(0.3)*PI+(0.3)*NE+(0.1)*PP

NE = round(PF, 1)

print(NE)
