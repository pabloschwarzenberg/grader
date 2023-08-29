#Cálculo del dígito verificador de un rut
def dv(rut):
	rut1=str(rut)[::-1]
	factor=2
	suma=0

	for i in rut1:
		suma+=int(i)*factor
		factor+=1
		if factor==8:
			factor=2

	dv=11-(suma%11)

	if dv== 10:
		return 'K'

	elif dv==11:
		return '0'

	else:
		return str(dv)

rut=int(input('Ingrese RUT sin puntos ni digito verificador: '))

dv=dv(rut)
print('dv=',dv)