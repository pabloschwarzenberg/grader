#Nota final
PT=float(input('Ingrese su nota de tareas: '))
PI=float(input('Ingrese su nota de interrogaciones: '))
NE=float(input('Ingrese su nota de examen: '))
PP=float(input('Ingrese su nota de presentacion: '))

Promedio_final=0.3*PT+0.3*PI+0.3*NE+0.1*PP


print('Su promedio final es',round(Promedio_final,1))
      