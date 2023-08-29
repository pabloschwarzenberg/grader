#Contestador de celular
num=input('Ingrese numero telefonico:')
if len(num)!=8:
 print('Error! El numero de telefono debe tener 8 cifras.')
else:
 num=int(num)
 a=str(num)[0]
 b=str(num)[1]
 c=str(num)[2]
 hr=int(input('Ingrese hora de la llamada:'))
 if 0<=hr<23:
 #condicionales
  if 19<=hr<=23:
   print('NO CONTESTAR')
  if 0<=hr<=7:
   print('CONTESTAR')
  if 7<hr<=13:
      if num%1000==909:
          print('CONTESTAR')
      else:
          print('NO CONTESTAR')
  if 16<hr<=19:
    
    if (a==8, b==7, c==7):
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
 else:
  print('Error! La hora debe ser un numero entero entre 0 y 23')


