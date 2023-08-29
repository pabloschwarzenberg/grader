#Contestador de celular
      #contestadora
tel=(input("escriba su numero de telefono: "))
hora=int(input("escriba la hora de llamada: "))
if hora>=0 and hora<=7:
  print("CONTESTAR")
elif tel[5]=="9" and tel[6]=="0" and tel[7]=="9":
    print("CONTESTAR")
elif hora>7 and hora<14:
  print("NO CONTESTAR")
elif tel[0]=="8" and tel[1]=="7" and tel[2]=="7":
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
  print("CONTESTAR")
elif hora>19:
 print("NO CONTESTAR")
else:
  print("NO CONTESTAR")