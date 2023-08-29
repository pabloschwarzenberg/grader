#Contestador de celular
celphone=(input('Ingrese numero de telefono:'))
if len(celphone)>8:
    print('numero',celphone,'invalido, ingrese otro numero')
hora=int(input('ingrese hora de llamada:'))
if hora>=0 and hora<=7:
    print('Contestar')
elif hora<14:
    if celphone[-1]=='9' and celphone[-2]=='0' and celphone[-3]=='9':
       print('Contestar')
    else:
         print('No contestar')
elif hora>=17 and hora<=19:
    if celphone[0]=='8' and celphone[1]=='7' and celphone[2]=='7':
        print('No contestar')
elif hora>19:
    print('No contestar')
