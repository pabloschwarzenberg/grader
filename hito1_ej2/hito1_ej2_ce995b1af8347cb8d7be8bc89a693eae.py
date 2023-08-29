#Contestador de celular
a=int(input())
b=int(input())
if b>0 and b<7:
  print('CONTESTAR')
elif b>7 and b<14 and (a%1000)!=909:
  print('NO CONTESTAR')
elif b>7 and b<14 and (a%1000)==909:
  print('CONTESTAR')
elif b>17 and b<19 and (a//100000)==877:
  print('NO CONTESTAR')
elif b>17 and b<19 and (a//100000)!=877:
  print('CONTESTAR')
else:
  print('NO CONTESTAR')
