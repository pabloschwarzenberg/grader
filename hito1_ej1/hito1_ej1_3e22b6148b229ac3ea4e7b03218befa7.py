#Nota final
PT = eval(input('Ingrese su nota de Tareas: '))
PI = eval(input('Ingrese su nota de Interrogaciones: '))
NE = eval(input('Ingrese su nota de Examen: '))
PP = eval(input('Ingrese su nota de Presentaciones: '))

print('Tu promedio final es', round(0.3*PT+0.3*PI+0.3*NE+0.1*PP, 1))