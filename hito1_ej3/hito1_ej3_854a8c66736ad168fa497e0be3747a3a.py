#Aprobación de créditos
import datetime
sueldo=int(input("Ingrese su sueldo en pesos: "))
anoDeNacimiento=int(input("Ingrese año de nacimiento: "))
numeroDeHijos=int(input("Ingrese el numero de hijos: "))
antiguedadCliente=int(input("Ingrese años de pertenencia al banco: "))
estadoCivil=input("Estado Civil (S=soltero, C=casado): ")
estadoCivil=estadoCivil.upper()
localidad=input("Si vive en campo digite (R), si vive en ciudad digite (U): ")
localidad=localidad.upper()
ano=datetime.datetime.now().year
edad = (ano - anoDeNacimiento)
veredicto="RECHAZADO"

if (antiguedadCliente>10 and numeroDeHijos>=2):
    veredicto="APROBADO"
if (estadoCivil=="C" and numeroDeHijos>3 and (edad>=45 and edad<=55)):
    veredicto="APROBADO"
if(sueldo>2500000 and estadoCivil=="S" and localidad=="U"):
    veredicto="APROBADO"
if(sueldo>3500000 and antiguedadCliente>5):
    veredicto="APROBADO"
if(estadoCivil=="C" and localidad=="R" and numeroDeHijos<2):
    veredicto="APROBADO"
print(veredicto)    