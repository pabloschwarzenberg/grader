#Nota final
 #NOTAS
PT = float(input('Ingrese notas Tareas:  '))
PI = float(input('Ingrese notas Interrogaciones: '))
NE = float(input('Ingrese notas Examen: '))
PP = float(input('Ingrese notas Presentación: '))
prom = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
pm= round(prom,1)
print('El promedio final es de ',(pm),'')  