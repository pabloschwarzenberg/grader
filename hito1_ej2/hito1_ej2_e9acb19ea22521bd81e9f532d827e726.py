#Contestador de celular
N = int(input('ingresa un numero de telefono: '))
hora = eval(input('ingresa la hora de llamada: '))


if hora  <= 7:
    print('contestar')

elif hora <= 14:
    if N % 1000==909:
        print('contestar')
    else:
        print('no contestar')
elif 17 <= N <=19:
    if N % 1000 == 877:
        print('no contestar')
    else:
        print ('contestar')

else:
    print('no contestar')
      