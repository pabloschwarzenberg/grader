N=int(input("Ingrese numero telefonico:"))
H=int(input("Ingrese hora de la llamada:"))
if H>0 and H<=7:
  print("CONTESTAR")
elif H>7 and H<=14:
  if str(N)[-3:]=="909":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif H>=17 and H<=19:
  if str(N)[:3]=="877":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
else:
  print("NO CONTESTAR")