#Contestador de celular
 
num = []
num.append(input('Ingrese numero telefonico: '))
num.append(input('Ingrese hora de llamada: '))
cel = num[0]
hra = int(num[1])

if hra >=0 and hra <=7:
  print('CONTESTAR')

if hra >7 and hra <14:
  if int(cel[-3:]) == 909:
     print('CONTESTAR')
  else:
     print('NO CONTESTAR')
  
if hra >=17 and hra <=19:
   if int(cel[0:3]) == 877:
     print('NO CONTESTAR')
   else:
     print('CONTESTAR')
     
if hra >19 and hra <=23:
    print('NO CONTESTAR') 