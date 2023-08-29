print('Postulacion de credito')
	
sueldo=int(input('Ingrese Sueldo en Pesos: '))
tiempo=int(input('Hace Cuanto es Cliente del Banco: '))
edad=int(input('Ingrese Edad:'))
hijos=int(input('Ingrese cantidad de Hijos: '))
ec=input('Ingrese Estado Civil (S de soltero y C si esta casado): ')
sector=input('Sector donde vive (U para urbano y R para rural): ')
if(tiempo>=11 and hijos>=2):
	print('APROBADO')

elif(ec=='C' and hijos<=4 and edad<=45 and edad>=55):
	print('APROBADO')

elif(sueldo<2500000 and ec=='S' and sector=='U'):
	print('APROBADO')

elif(sueldo<3500000 and tiempo>=6):
	print('APROBADO')

elif(sector=='R' and ec=='C' and hijos<2):
	print('APROBADO')
else:
	print('RECHAZADO')