#Aprobación de créditos
def aprobarcredito(ingresomensual, anonacimiento, hijos, datosbanco, estadocivil, lugarderesidencia):
	if datosbanco>10 and hijos>=2:
		return True
	elif estadocivil=='C' and hijos>3 and 45<=(2023 - anonacimiento) <= 55:
		return True
	elif ingresomensual>2500000 and estadocivil=='S' and lugarderesidencia=='U':
		return True
	elif ingresomensual>3500000 and datosbanco>5:
		return True
	elif lugarderesidencia=='R' and estadocivil=='C' and hijos<2:
		return True
	else:
		return False


ingresomensual=int(input('Ingrese el ingresomensual mensual en pesos: '))
anonacimiento=int(input('Ingrese el ano de anonacimiento: '))
hijos=int(input('Ingrese el numero de hijos: '))
datosbanco=int(input('Ingrese los anos de pertenencia al datosbanco: '))
estadocivil=input('Ingrese el estado estadocivil ("S" para soltero, "C" para casado): ')
lugarderesidencia=input('Ingrese el lugar de lugarderesidencia ('U' para urbano, 'R' para rural): ')


estado=aprobarcredito(ingresomensual, anonacimiento, hijos, datosbanco, estadocivil, lugarderesidencia)

if estado:
	print('APROBADO')
else:
	print('RECHAZADO')      