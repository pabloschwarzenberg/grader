#Contestador de celular
n=eval(input('Ingrese numero telefonico:'))
h=eval(input('Ingrese hora de la llamada:'))
u3d= n%1000
       
if(h>=0 and h<=7):
    print('contestar')
elif(h<14 and u3d==909):
          print('contestar')
elif(h>=17 and h<=19 and u3d==877):
          print('no contestar')
elif(h>=19):
          print('no contestar')
else:
          print('no contestar')
