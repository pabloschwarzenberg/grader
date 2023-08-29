#Contestador de celular

Telefono=int(input('Ingrese el número telefónico de 8 cifras: '))
DigitosTelefono=len(str(Telefono))

while DigitosTelefono!=8:
    Telefono=int(input('\nEl número ingresado es incorrecto. Ingrese nuevamente el número telefónico de 8 cifras: '))
    DigitosTelefono=len(str(Telefono))

TextoTelefono=str(Telefono)          

HoraLlamada=int(input('\nIngresa la hora de la llamada: '))

while HoraLlamada<0 or HoraLlamada>23:
    HoraLlamada=int(input('\nLa hora ingresada es incorrecta. Ingresa la hora de la llamada nuevamente: '))

if 0<= HoraLlamada <= 7:
                    print('\nDebes CONTESTAR, puede ser una emergencia!')

if 8<=HoraLlamada<=13:
    if TextoTelefono[-1]=='9' and TextoTelefono[-2]=='0' and TextoTelefono[-3]=='9':
         print('\nDebes CONTESTAR')

    else:
        print('\n NO CONTESTAR')

if 14<=HoraLlamada<=16:
        print('\nNO CONTESTAR')


if 17<=HoraLlamada<=19:
     if TextoTelefono[0]=='8' and TextoTelefono[1]=='7' and TextoTelefono[2]=='7':
         print('\nNO CONTESTAR')

     else:
        print('\nDebes CONTESTAR')

if HoraLlamada>19:
    print('\nNO CONTESTAR')
      