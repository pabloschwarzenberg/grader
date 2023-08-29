#Descomponer un número
import sys

def DescomponerNro(nro):
	
	if nro>=0 and nro<10000:
	
		unidades=nro%10
		decenas=(nro//10)%10
		centenas=(nro//100)%10
		miles=nro//1000

		desnr=''
		
		if nro<10:
			
			if unidades>=0:
				desnr+=str(unidades)+'U'

		if nro>=10 and nro<100:
		
			if decenas>=0:
				desnr+=str(decenas)+'D+'
			if unidades>=0:
				desnr+=str(unidades)+'U'
		
		if nro>=100 and nro<1000:
			if centenas>=0:
				desnr+=str(centenas)+'C+'
			if decenas>=0:
				desnr+=str(decenas)+'D+'
			if unidades>=0:
				desnr+=str(unidades)+'U'
				
		if nro>=1000 and nro<10000:
			
			if miles>=0:
				desnr+=str(miles)+'M+'
			if centenas>=0:
				desnr+=str(centenas)+'C+'
			if decenas>=0:
				desnr+=str(decenas)+'D+'
			if unidades>=0:
				desnr+=str(unidades)+'U'

		return desnr
		
	else:
		
		print('')
		print('SOLO HASTA 4 DIGITOS')
		sys.exit(0)

nro=int(input('Ingrese un numero entero de hasta 4 digitos: '))

des=DescomponerNro(nro)

print('')

print(des)