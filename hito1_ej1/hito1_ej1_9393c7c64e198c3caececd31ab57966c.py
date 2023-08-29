#Nota final
pt = float(input('Introduzca nota tareas:'))
pi = float(input('Introduzca nota interrogaciones:'))
ne = float(input('Introduzca nota Examen:'))
pp = float(input('Introduzca nota Presentacion:'))

nota_final = round(0.3*pt+0.3*pi+0.3*ne+0.1*pp, 1)
print('su nota final es', nota_final)      