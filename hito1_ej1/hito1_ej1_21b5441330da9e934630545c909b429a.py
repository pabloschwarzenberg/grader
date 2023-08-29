#Nota final
pt = eval(input('Ingrese nota de tareas:'))
pi = eval(input('Ingrese nota de interrogaciones:'))
ne = eval(input('Ingrese nota de examen:'))
pp = eval(input('Ingrese nota de presentación:'))
print('\n')
nf = 0.3*pt+0.3*pi+0.3*ne+0.1*pp
nff = round(nf,1)
print('Su nota final es:',nff)