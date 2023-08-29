#Aprobación de créditos
import datetime
sueldo=int(input('Ingrese su sueldo en pesos:'))
AnoNacimiento=int(input('Ingrese el año de nacimiento:'))
NumerodeHijos=int(input('Ingrese el numero de hijos:'))
AntiguedadCliente=int(input('Ingrese años de pertenencia al banco'))
EstadoCivil=input('Estado Civil (S=Soltero, C=Casado):')
EstadoCivil=EstadoCivil.upper()
localidad=input('Si vive en campo digite (R), Si vive en ciudad digite (U):')
localidad=localidad.upper()
ano=datetime.datetime.now().year
edad=(ano - AnoNacimiento)
veredicto='RECHAZADO'

if (AntiguedadCliente>10 and NumerodeHijos>=2):
  veredicto='APROBADO'
if(EstadoCivil=='C' and NumerodeHijos>3 and (edad>=45 and edad<=55)):
  veredicto='APROBADO'
if(sueldo>2500000 and EstadoCivil=='S' and localidad=='U'):
  veredicto='APROBADO'
if(sueldo>3500000 and AntiguedadCliente>5):
  veredicto='APROBADO'
if(EstadoCivil=='C' and localidad=='R' and NumerodeHijos<2):
  veredicto='APROBADO'
print(veredicto)
