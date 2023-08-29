#Contestador de celular
#solicitar un numero telefonico y hora de la llamada 
numero_telefonico=int(input('ingrese el numero telefonico: ')) 
hora_llamada=int(input('ingrese hora de la llamada: '))
#reglas para contestar una llamada
if hora_llamada >= 0 and hora_llamada <= 7:
    print('resultado: contestar')
elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
    print('resultado: contestar')
elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico)[:3] != '877':
    print('resultado: contestar')
else:
    print('resultado: no contestar')

      