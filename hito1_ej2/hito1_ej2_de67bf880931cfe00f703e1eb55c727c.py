#Contestador de celular
num_celular=int(input('Ingrese numero telefonico:',))
hora=int(input('Ingrese hora de la llamada:',))
if 0<=hora and hora<=7:
   print('CONTESTAR')
elif 7<hora and hora<14 and num_celular%1000==909:
   print('CONTESTAR')
elif 7<hora and hora<14:
   print('NO CONTESTAR')
elif 17<hora and hora<19 and num_celular//87700000==1: 
    print('NO CONTESTAR')
elif 14<hora and hora<17:
    print('CONTESTAR')
elif 17<hora and hora<19:
    print('CONTESTAR')
elif 19<hora and hora<23:
    print('NO CONTESTAR')