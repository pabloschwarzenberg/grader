#Contestador de celular
n=eval(input('Ingrese numero telefonico:'))
h=eval(input('Ingrese hora de la llamada:'))
ultimos3digitos= n%1000
primeros3digitos=round(n/100000)
       
if(h>=0 and h<=7):
    print('contestar')
elif(h<14 and ultimos3digitos!=909):
          print('no contestar')
elif(h>=17 and h<=19 and primeros3digitos!=877):
          print('no contestar')
elif(h>=19):
          print('no contestar')
else:
          print('contestar')