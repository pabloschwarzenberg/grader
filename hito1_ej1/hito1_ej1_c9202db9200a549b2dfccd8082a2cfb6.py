#Nota final

PT = eval(input('Tareas: '))
PI = eval(input('Interrogaciones: '))
NE = eval(input('Examen: '))
PP = eval(input('Presentacion: '))

a = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

ro = round(a,1)

print(ro)