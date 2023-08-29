#Contestador de celular
telefono=(input("ingrese numero de telefono"))
if len(telefono)>8:
   print("numero",telefono,"invalido,ingrese otro numero")
hora=float(input("ingrese una hora"))
if hora>=0 and hora<=7:
   print("contestar")
elif hora<14:
   if telefono[-1]=='9'and telefono[-2]=='0'and telefono[-3]=='9':
      print("contestar")
   else:
      print("no contestar")
elif hora>=17and hora<=19:
   if telefono[0]=='8'and telefono[1]=='7' and telefono[2]=='7':
      print("no contestar")
elif hora>19:
   print("no contestar")