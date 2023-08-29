telefono=list(input("ingrese numero telefonico:"))
hora=int(input("ingrese hora de llamda:"))
if hora>=0 and hora<=7:
  print("CONTESTAR")
elif hora>7 and hora<14:
  if telefono[-1]=="9" and telefono[-2]=="0" and telefono[-3]=="9":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
  if telefono[0]=="8" and telefono[1]=="7" and telefono[2]=="7":
    print("NO CONTESTAR")
  else:
    print("COTESTAR")
else:
  print("NO CONTESTAR")