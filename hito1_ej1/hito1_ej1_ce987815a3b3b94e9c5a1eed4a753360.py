#Nota final
PT = eval(input('Ingrese notas de tareas: '))
PI = eval(input('Ingrese notas de interrogaciones: '))
NE = eval(input('Ingrese notas de exámen: '))
PP = eval(input('Ingrese notas de presentación: '))

if PT == 1 or PT == 2 or PT == 3 or PT == 4 or PT == 5 or PT == 6 or PT == 7:
  print('Calcular:',0.3*PT )
  
if PI == 1 or PI == 2 or PI == 3 or PI == 4 or PI == 5 or PI == 6 or PI == 7:
  print('Calcular:',0.3*PI )
  
if NE == 1 or NE == 2 or NE == 3 or NE == 4 or NE == 5 or NE == 6 or NE == 7:
  print('Calcular:',0.3*NE )
  
if PT == 1 or PP == 2 or PP == 3 or PP == 4 or PP == 5 or PP == 6 or PP == 7:
  print('Calcular:',0.1*PP )

promedio = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP,1)
print('El promedio es: ', promedio)