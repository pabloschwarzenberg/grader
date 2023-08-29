#Contestador de celular
contestar = False

telefono = (input('Ingrese numero telefonico: '))
#validando el largo del numero
while len(telefono) != 8:
    telefono = (input('Ingrese numero telefonico: '))


hora = int((input('Ingrese hora de la llamada: ')))
#validando que la hora ingresada este dentro del rango permitido
while hora < 0 or hora > 23:
    hora = int((input('Ingrese hora de la llamada: ')))

if 0 <= hora <= 7:
    contestar = True
elif hora < 14 and telefono[5:] == '909':
    contestar = True
elif (17 <= hora <= 19) and (telefono[:3] != '877'):
    contestar = True

if contestar:
    print('CONTESTAR')
else:
    print('NO CONTESTAR')