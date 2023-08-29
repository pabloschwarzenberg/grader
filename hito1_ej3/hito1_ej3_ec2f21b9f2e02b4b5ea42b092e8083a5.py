#Aprobación de credito
ingreso=int(input('ingrese su ingreso en pesos'))
ano=int(input('ingrese su año de nacimiento'))
hijos=int(input('ingrese numero de hijos'))
pertenencia=int(input('ingrese sus años en el banco'))
estado=input('ingrese S si esta soltero o C si esta casado')
vive=input('ingrese U si vive en ciudad o R si vive en el campo')
if((2018-pertenencia)>10)and(hijos>=2):
  print('APROBADO')
elif(estado=='C')and(hijos==3)and((2018-ano<55)and(2018-ano>45)):
  print('APROBADO')
elif(ingreso>2500000)and(estado=='S')and(vive=='U'):
  print('APROBADO')
elif(ingreso>3500000)and((2018-pertenencia)>5):
  print('APROBADO')
elif(vive=='R')and(estado=='C')and(hijos<2):
  print('APROBADO')
else:
  print('RECHAZADO')