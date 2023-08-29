#Aprobación de créditos
    #Aprobación de créditos
def aprobarcredito(ingreso, nacimiento, hijos, banco, civil, residencia):
	if banco>10 and hijos>=2:
		return True
	elif civil=='C' and hijos>3 and 45<=(2023 - nacimiento) <= 55:
		return True
	elif ingreso>2500000 and civil=='S' and residencia=='U':
		return True
	elif ingreso>3500000 and banco>5:
		return True
	elif residencia=='R' and civil=='C' and hijos<2:
		return True
	else:
		return False


ingreso=int(input('Ingrese el ingreso mensual en pesos: '))
nacimiento=int(input('Ingrese el ano de nacimiento: '))
hijos=int(input('Ingrese el numero de hijos: '))
banco=int(input('Ingrese los anos de pertenencia al banco: '))
civil=input('Ingrese el estado civil ("S" para soltero, "C" para casado): ')
residencia=input('Ingrese el lugar de residencia ('U' para urbano, 'R' para rural): ')


aprobado=aprobarcredito(ingreso, nacimiento, hijos, banco, civil, residencia)

if aprobado:
	print('APROBADO')
else:
	print('RECHAZADO')  