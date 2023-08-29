#Nota final
PT =float(input('ingrese nota tareas: '))
PI =float(input('ingrese nota interrogaciones: '))
NE =float(input('ingrese nota Examen: '))
PP =float(input('ingrese nota presentacion: '))

final = 0.3*PT+0.3*PI+0.3*NE+0.1*PP

final=round(final,1)
print(final)