#Contestador de celular
cel=int(input("Ingrese numero telefonico:"))
h=int(input("Ingrese hora de llamada:"))

if h>=19:
  print("NO CONTESTAR")
if 17<=h<=19:
  if cel==87765545:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if 0<=h<7:
  print("CONTESTAR")
if 7<=h<=14 and (cel==77389909):
  print("CONTESTAR")