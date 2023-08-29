#Contestador de celular
fono = int(input())
hora = int(input())
if hora>=0 and hora <=7:
  print("CONTESTAR")  
if hora>7 and hora <14:
  if (fono%1000)== 909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if hora>14 and hora<17:
  print("NO CONTESTAR")
if hora>=17 and hora<=19:
  if fono//100000 == 877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if hora >19:
  print("NO CONTESTAR")