#Contestador de celular
nm=eval(input('Ingrese numero telefonico: '))
h=eval(input('Ingrese hora de llamada: '))
l3=nm%1000
p3=nm//1000
if h>=0 and h<=7:
  print('CONTESTAR')
elif h<14 and l3==909:
  print('CONTESTAR')
elif h>=17 and h<=19 and p3==877:
  print('NO CONTESTAR')
else:
  print('NO CONTESTAR')