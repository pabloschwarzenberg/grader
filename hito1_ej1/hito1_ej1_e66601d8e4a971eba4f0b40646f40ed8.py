#Nota final
pt=eval(input('ingrese la nota de "tareas":'))
pi=eval(input('ingrese la nota de "interrogaciones":'))
ne=eval(input('ingrese la nota de "examen":'))
pp=eval(input('ingrese la nota de "presentacion":'))


print(round( 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp,1))
