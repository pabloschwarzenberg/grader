#Aprobación de créditos
from datetime import datetime
fecha = datetime.now()
datos = []
datos.append(input('Ingreso (en pesos)                      : ')) #0
datos.append(input('Año de nacimiento                       : ')) #1
datos.append(input('Numero de hijos                         : ')) #2
datos.append(input('Años de pertenencia al banco            : ')) #3
datos.append(input('Estado civil("S" soltero, "C" casado )  : ')) #4
datos.append(input('Lugar donde vive ("U" urbano, "R" rural): ')) #5
edad = fecha.year - int(datos[1])


if int(datos[3]) >= 10 and int(datos[2]) >= 2:
    print('APROBADO')
if datos[4] == 'C' and int(datos[2]) > 3 and edad > 44 and edad <56:
    print('APROBADO')
if int(datos[0]) > 2500000 and datos[4] == 'S' and datos[5] == 'U':
    print('APROBADO')
if int(datos[0]) > 3500000 and int(datos[3]) > 5:
    print('APROBADO')
if datos[5] == 'R' and datos[4] == 'C' and int(datos[2]) < 3:
    print('APROBADO')   