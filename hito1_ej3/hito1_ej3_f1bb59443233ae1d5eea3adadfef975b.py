from datetime import datetime
fecha = datetime.now()
info = []
info.append(input('Ingreso (en pesos)                      : ')) 
info.append(input('Año de nacimiento                       : ')) 
info.append(input('Numero de hijos                         : ')) 
info.append(input('Años de pertenencia al banco            : ')) 
info.append(input('Estado civil("S" soltero, "C" casado )  : ')) 
info.append(input('Lugar donde vive ("U" urbano, "R" rural): ')) 
edad = fecha.year - int(info[1])


if int(info[3]) >= 10 and int(info[2]) >= 2:
    print('APROBADO')
if info[4] == 'C' and int(info[2]) > 3 and edad > 44 and edad <56:
    print('APROBADO')
if int(info[0]) > 2500000 and info[4] == 'S' and info[5] == 'U':
    print('APROBADO')
if int(info[0]) > 3500000 and int(info[3]) > 5:
    print('APROBADO')
if info[5] == 'R' and info[4] == 'C' and int(info[2]) < 3:
    print('APROBADO')