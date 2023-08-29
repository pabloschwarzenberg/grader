#Zodiaco
diaNacimiento = eval(input('Ingrese su dia de nacimiento: '))    
mesNacimiento = eval(input('Ingrese su mes de nacimiento: '))

if(mesNacimiento==3 and 21<=diaNacimiento<=31) or (mesNacimiento==4 and 21>diaNacimiento>=1):
  print('aries')
elif(mesNacimiento==4 and 21<=diaNacimiento<=30) or (mesNacimiento==5 and 21>diaNacimiento>=1):
  print('tauro')
elif(mesNacimiento==5 and 21<=diaNacimiento<=31) or (mesNacimiento==6 and 21>diaNacimiento>=1):
  print('geminis')
elif(mesNacimiento==6 and 21<=diaNacimiento<=30) or (mesNacimiento==7 and 23>diaNacimiento>=1):
  print('cancer')
elif(mesNacimiento==7 and 21<=diaNacimiento<=31) or (mesNacimiento==8 and 21>diaNacimiento>=1):
  print('leo')
elif(mesNacimiento==8 and 21<=diaNacimiento<=30) or (mesNacimiento==9 and 21>diaNacimiento>=1):
  print('virgo')
elif(mesNacimiento==9 and 21<=diaNacimiento<=30) or (mesNacimiento==10 and 21>diaNacimiento>=1):
  print('libra')
elif(mesNacimiento==10 and 21<=diaNacimiento<=31) or (mesNacimiento==11 and 22>diaNacimiento>=1):
  print('escorpion')
elif(mesNacimiento==11 and 21<=diaNacimiento<=30) or (mesNacimiento==12 and 22>diaNacimiento>=1):
  print('sagitario')
elif(mesNacimiento==12 and 21<=diaNacimiento<=31) or (mesNacimiento==1 and 20>diaNacimiento>=1):
  print('capricornio')
elif(mesNacimiento==1 and 21<=diaNacimiento<=31) or (mesNacimiento==2 and 19>diaNacimiento>=1):
  print('acuario')
elif(mesNacimiento==2 and 21<=diaNacimiento<=28) or (mesNacimiento==3 and 21>diaNacimiento>=1):
  print('piscis')
