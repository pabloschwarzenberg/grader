#Nota final
PT = float(input('Notas Tareas: '))
PI = float(input('Notas Interrogaciones: '))
NE = float(input('Nota Examen: '))
PP = float(input('Nota Presentacion: '))

X = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

print(round(X,1))
