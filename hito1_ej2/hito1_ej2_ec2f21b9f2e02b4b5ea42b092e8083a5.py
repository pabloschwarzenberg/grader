#Contestador de celular
lista=[]

numero=input('ingrese el numero')
lista.append(numero)
hora=int(input('ingrEse la hora de la llamada'))

if(hora>=12 and hora<=7):
    print('CONTESTAR')
elif(hora<=14):
    p=numero[-1]+numero[-2]+numero[-3]
    if(p=='909'):
      print('CONTESTAR')
    else:
      print('CONTESTAR')
    
if(hora<=19 and hora>=17):
    o=numero[0]+numero[1]+numero[2]
    if(o=='877'):
      print('NO CONTESTAR')
    else:
      print('CONTESTAR')

elif(hora>=19):
  print('NO CONTESTAR')