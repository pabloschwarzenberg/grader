#Contestador de celular
print("Para contestar número")
tel = input("Número de telefono:")
hra = int(input("Hora actual:"))
if 0<=hra<=23:
  if 0<=hra<7:
    print("CONTESTAR")
  if 7<hra<14:
    if eval(tel[5]+tel[6]+tel[7])==909:
      print("CONTESTAR")
    else:
      print("NO CONTESTAR")
  if 14<=hra<17:
    print("NO CONTESTAR")
  if 17<=hra<=19:
    if eval(tel[0]+tel[1]+tel[2])==877:
      print("NO CONTESTAR")
    else:
      print("CONTESTAR")
  if 19<hra:
    print("NO CONTESTAR")
else:
  print("Hora inexistente")
    