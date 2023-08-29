#Nota final
print('=====Ingrese 4 notas para que el programa calcule su promedio=====')






PT = float(input('Ingrese las notas obtenidas en sus tareas: '))
PI = float(input('Ingrese las notas obetenidas en sus interrogaciones: '))
NE = float(input('Ingrese la nota obtenida su su examen: '))
PP = float(input('Ingrese la nota obtenida en su presentación: '))

promedio= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print('El promedio obtenido es: ',round(promedio,1))
