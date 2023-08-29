#Nota final
PT=float(input('Ingrese el promedio de sus tareas: '))
print('')
PI=float(input('Ingrese el promedio de sus interrogaciones: '))
print('')
NE=float(input('Ingrese la nota de su examen: '))
print('')
PP=float(input('Ingrese la nota de su presentacion: '))

NF=(PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1)

print('')
print('Su nota final es: '+str(round(NF,1)))
print('')