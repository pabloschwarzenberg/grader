#Contestador de celular
Telefono = int(input('ingresa tu celular de 8 digitos: '))
Hora = int(input('ingresa la hora: '))

excepcion1=(Telefono%1000)
excepcion2=(Telefono//100000)

if 0<= Hora <=7:
    print('CONTESTAR')
if 8<= Hora <=14 and excepcion1 == 909:
    print('CONTESTAR')
elif 8<= Hora <=14:
    print('NO CONTESTAR')
if 17<= Hora <=19 and excepcion2 == 877:
    print('NO CONTESTAR')
elif 17<= Hora <=19:
    print('CONTESTAR')
if Hora>19:
    print('NO CONTESTAR')
