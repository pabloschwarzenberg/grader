#Nota final
PT=float(input('ingrese la nota final de tareas: ', ))
PI=float(input('Ingrese la nota de las interrogaciones: ', ))
NE=float(input('Ingrese la nota de el examen: ', ))
PP=float(input('Ingrese la nota de la presentación: ',))
NotaFinal= float((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
print('Su promedio de notas es de:', round(NotaFinal, 1)) 
