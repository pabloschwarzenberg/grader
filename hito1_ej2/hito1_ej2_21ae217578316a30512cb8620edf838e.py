#Contestador de celular
tel= int(input())
hora=int(input())

if hora >= 0 and hora <=7:
  print('CONTESTAR')
elif hora< 14:
   if (tel % 1000)==909:
      print('CONTESTAR')
   else:
      print('NO CONTESTAR')
elif hora>= 17 and hora<=19:
   if(tel//100000)== 877:
      print('NO CONTESTAR')
   else:
      print('CONTESTAR')
elif hora> 19:
   print('NO CONTESTAR')
else:
   print('CONTESTAR')