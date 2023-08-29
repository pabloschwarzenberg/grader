#Contestador de celular
x = int(input('Ingrese un numero telefonico de 8 cifras: '))
y = eval(input('Ingrese la hora de la llamada: '))

if 0<=y<=7:
    print('contestar')
if y<14 and x%1000==909:
    print ('contestar')
if 17<=y<=19 and (x//100000==877):
        print('no contestar')
if 19<=y:
        print('no contestar')