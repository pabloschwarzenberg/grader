#Nota final
pt = eval(input('Ingrese la Nota de tareas:'))
pi = eval(input('Ingrese la Nota de Interrogaciones:'))
ne = eval(input('Ingrese la Nota de Examen:'))
pp = eval(input('Ingrese la Nota de Presentación:'))

promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print('El promedio final es:',round(promedio,1))