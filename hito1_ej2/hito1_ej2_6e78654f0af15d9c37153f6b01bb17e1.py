#Contestador de celular
NumeroTelefono= input('Introducir numero de telefono: ')
if len(NumeroTelefono) !=8:
    print ('Error, no es un numero de telefono')
HoraDelLlamado= int(input('Introducir hora del llamado en formato 24hrs: '))
if (HoraDelLlamado) >= 00 and (HoraDelLlamado) <= 7:
    print ('Contestar, puede ser una emergencia')
if ((HoraDelLlamado < 14) and (NumeroTelefono[-3:]=='909')):
    print ("Contestar")
if (HoraDelLlamado) <= 12:
    print ('No contestar')
if (HoraDelLlamado) >= 17 and (HoraDelLlamado) <= 19 and (NumeroTelefono[0:3]=='877'):
    print ('No contestar')
if (HoraDelLlamado) >= 17 and (HoraDelLlamado) <= 19 and (NumeroTelefono[0:3]!='877'):
    print ('Contestar')
if (HoraDelLlamado) > 19:
    print ('No contestar')