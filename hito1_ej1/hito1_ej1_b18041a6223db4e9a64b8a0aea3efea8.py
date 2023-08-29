#Nota final
print('Programa para calcular tu promedio final: ')

pt = eval(input('Inserte el promedio de sus tareas: '))
pi = eval(input('Inserte el promedio de sus interrogaciones: '))
ne = eval(input('Inserte la nota de su examen: '))
pp = eval(input('inserte la nota de su presentación: '))
promfinal = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
promfinal_undecimal = round(promfinal,1)

print('Su promedio final es: ', promfinal_undecimal)