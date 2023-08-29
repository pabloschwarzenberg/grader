#Nota final

print('\nIngresa las siguientes 4 notas.')

pt = float(input('\nNota de Tarea: '))
pi = float(input('Nota de Interrogación: '))
ne = float(input('Nota de Exámen: '))
pp = float(input('Nota de Presentación: '))

promedio = pt*0.3 + pi*0.3 + ne*0.3 + pp*0.1

print(round(promedio, 1))