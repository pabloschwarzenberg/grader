#Nota final
NT= float(input('ingrese la nota de Tareas: '))
NI= float(input('ingrese la nota de Interrogaciones: '))
NE= float(input('ingrese la nota de Examen: '))
NP= float(input('ingrese la nota de Presentación: '))
e=(0.3*NT)+(0.3*NI)+(0.3*NE)+(0.1*NP)
print(round(e,1))     