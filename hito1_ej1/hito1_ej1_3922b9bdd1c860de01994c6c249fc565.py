#Nota final
print('introduce la primera nota')
PT=input('ingrese nota de tarea:')
print('introduce la primera nota')
PI=input('ingrese nota de interrogaciones:')
print('introduce la primera nota')
NE=input('ingrese nota de examen:')
print('introduce la primera nota')
PP=input('ingrese nota de presentacion:')

PT=float(PT)
PI=float(PI)
NE=float(NE)
PP=float(PP)

#calcular el promedio
promedio=round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1)
print(promedio)

