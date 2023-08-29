#Aprobación de créditos
#VARIABLES#
ingresos=int(input('Ingresos: '))
añoNacimiento=int(input('Año de nacimiento: '))
nHijos=int(input('Número de hijos: '))
añosPertenencia=int(input('Años de pertenencia al banco: '))
estadoCivil=str.lower(input('Estado civil ("S": soltero, "C", casado): '))
lugarHogar=str.lower(input('Vive en un entorno rural (R) o urbano (U)?: '))
años=2022-añoNacimiento
#PROCESO#
if (añosPertenencia>10 and nHijos>=2) or (estadoCivil=='c' and nHijos>3 and 45<años<55) or (ingresos>2500000 and estadoCivil=='s' and lugarHogar=='u')\
     or (ingresos>3500000 and añosPertenencia>5) or (lugarHogar=='r' and estadoCivil=='c' and nHijos<2):
    print('APROBADO')
else:
    print('RECHAZADO')