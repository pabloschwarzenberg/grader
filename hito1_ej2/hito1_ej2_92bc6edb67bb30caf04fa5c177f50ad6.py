#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
if hora>19:
  print("NO CONTESTAR")
elif hora>=0 and hora<=7:
  print("CONTESTAR")
elif hora<14:
  if numero%1000==909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
  if (int(numero/100000))==877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")