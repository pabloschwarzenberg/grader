#Nota final
PT= float(input('ingrese la nota de Tareas: '))
PI= float(input('ingrese la nota de Interrogaciones: '))
NE= float(input('ingrese la nota de Examen: '))
PP= float(input('ingrese la nota de Presentación: '))
e=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print(round(e,1))