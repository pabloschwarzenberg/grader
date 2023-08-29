#Contestador de celular
n = str(input('Ingrese numero telefonico: '))
h = int(input('Ingrese hora de la llamada: '))
p = n [0:3]

f = n [5:8]

if h >= 0 and h <= 7:
    print('CONTESTAR')
elif h < 14:
    if f == '909':
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif h >= 17 and h <= 19:
    if p == '877':
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
elif h > 19:
    print('NO CONTESTAR')
      