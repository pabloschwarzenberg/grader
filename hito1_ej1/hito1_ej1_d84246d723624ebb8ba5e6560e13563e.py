#Nota final
PT=float(input('Ingrese nota de tarea: '))
PI=float(input('Ingrese nota de interrogaciones: '))
NE=float(input('Ingrese nota de examen: '))
PP=float(input('Ingrese nota de presentacion: '))
Promedio=(PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1)
Promedio=round(Promedio,1)
print('EL promedio ponderado de notas es : '+str(Promedio))