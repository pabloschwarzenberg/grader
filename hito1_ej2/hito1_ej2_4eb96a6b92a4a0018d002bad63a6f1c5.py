#Contestador de celular
telefono=(input("Ingresa numero telefonico: "))
hora=int(input("Ingresa hora de llamada: "))
if len(telefono)==8:
  if 0<=hora<=7:
    print("CONTESTAR")
  if 7<=hora<=14:
    if telefono[-3:]=="909":
      print("Contestar")
    else:
      print("NO CONTESTAR")
  if 17<=hora<=19:
    if telefono[0:3]=="877":
      print("NO CONTESTAR")
    else:
      print("CONTESTAR")
  if hora>=19:
    print("NO CONTESTAR")
      
