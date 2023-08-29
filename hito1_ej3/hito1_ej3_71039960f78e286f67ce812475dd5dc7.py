#Aprobación de créditos
from datetime import datetime

añoPrecente = int(datetime.today().strftime('%Y'))


ingresos = int(input("Ingreso: "))
añoNacimiento = int(input('Año Nacimiento: '))
numHijos = int(input('Numero de hijos: '))
añosPertenencia = int(input('Años de pertenencia al banco: '))
estadoCivil = input('Estado civil ("S" soltero , "C" casado):  ')
zonaVivienda = input('Vive en  ("U" urbano , "R" rural):  ')

edad = añoPrecente - añoNacimiento

if (añosPertenencia > 10 and numHijos >= 2):
    print("APROBADO")
elif (estadoCivil == 'C' and numHijos > 3 and (edad >=45 and edad <=55) ):
    print("APROBADO")
elif (ingresos > 2500000 and estadoCivil == 'S' and zonaVivienda == 'U'):
    print("APROBADO")
elif (ingresos > 3500000 and añosPertenencia > 5):
    print("APROBADO")
elif (zonaVivienda == 'R' and estadoCivil == 'C' and numHijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
    