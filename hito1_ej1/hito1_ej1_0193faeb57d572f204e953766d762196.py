#Nota final
PT= eval(input('Ingrese ptje de tareas:'))
PI= eval(input('Ingrese su ptje de Interrogaciones:'))
NE= eval(input('Ingrese su ptje del Examen:'))
PP= eval(input('Ingrese su ptje de la presentacion:'))

suma= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print('nota final:',suma)
round(suma,2)