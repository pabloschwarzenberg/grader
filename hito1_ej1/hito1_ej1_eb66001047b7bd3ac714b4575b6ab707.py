#Nota final
print('CALCULA TU PROMEDIO:')
pt=float(input('Ingrese promedio de tareas: '))
pi=float(input('Ingrese promedio de interrogaciones: '))
ne=float(input('Ingrese nota de examen: '))
pp=float(input('Ingrese nota presentacion: '))
prom=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
promedio=round(prom,1)
print('Tu promedio final es de: ', promedio)