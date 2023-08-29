##PT = Tareas
##PI = Interrogaciones
##NE= Examen
##PP = Presentacion
PT = float(input('ingrese nota tareas: '))
PI = float(input('ingrese nota interrogaciones: '))
NE = float(input('ingrese nota examen: '))
PP = float(input('ingrese nota presentacion: '))

#Nota final
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(promedio,1))
     