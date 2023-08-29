#Contestador de celular
telefono=int(input("Numero de telefono: "))
hora=int(input("Hora de llamada: "))
if 0<=hora<=7:
  print("CONTESTAR")
if 8<=hora<=14:
  if int(telefono%10**3)==909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if 17<=hora<=19: 
  if int(telefono/10**5)==877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if 20<=hora<=24:
  print("NO CONTESTAR")