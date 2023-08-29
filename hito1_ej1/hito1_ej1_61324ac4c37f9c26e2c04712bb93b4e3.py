#Nota final
pt=float(input('ingrese su nota de tareas: '))
pi=float(input('ingrese su nota de interrogaciones: '))
ne=float(input('ingrese su nota de examen: '))
pp=float(input('ingrese su nota de presentacion: '))
promedio=((3/10)*pt)+((3/10)*pi)+((3/10)*ne)+((1/10)*pp)  
print('su promedio es: ',round(promedio,1))
