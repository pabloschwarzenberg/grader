#Contestador de celular
telefono = int(input ("Ingrese número telefónico: "))
hora = int(input('Ingrese la hora: '))
if hora >= 0 and hora <= 7:
    print ('Contestar.')
if hora > 7 and hora <= 14:
    if telefono % 10 ** 3 == 909:
        print ('Contestar.')
    else:
        print ('No contestar.')
if hora >= 17 and hora <= 19:
    if telefono % 10 ** 3 == 877:
        print ('Contestar.')
    else:
        print ('No contestar.')
elif hora > 19 and hora <= 23:
    print ('No contestar.')