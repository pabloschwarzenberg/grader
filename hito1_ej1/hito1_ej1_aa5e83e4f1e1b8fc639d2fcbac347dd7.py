PT=0
PI=0
NE=0
PP=0

PT=int(input('Ingresa nota de tareas:'))
PI=int(input('Ingresa nota de interrogaciones:'))
NE=int(input('Ingresa nota de examen:'))
PP=int(input('Ingresa nota de presentacion:'))
if PT or PI or NE or PP (10>70):
    nota=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print('Su promedio final es:',round(nota))

