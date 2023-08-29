#Contestador de celular

telefono = int(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))

convertir = str(telefono)
primerosdigitos = convertir[0]+convertir[1]+convertir[2]
ultimosdigitos = convertir[5]+convertir[6]+convertir[7]

if hora >= 0 and hora <= 7:
    print('CONTESTAR')
elif hora < 14:
    if '909' in ultimosdigitos:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif hora >= 17 and hora <= 19:
    if '877' in primerosdigitos:
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
elif hora > 19:
    print('NO CONTESTAR')
else:
    print('NO CONTESTAR')