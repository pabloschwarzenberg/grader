#Nota final

PT=float(input('Ingrese nota en tareas:'))
PI=float(input('Ingrese nota en interrogaciones:'))
NE=float(input('Ingrese nota de examen:'))
PP=float(input('Ingrese nota de presentacion:'))

x=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
r=round(x, 1)
print('Su promedio final es:',' ',str(r))