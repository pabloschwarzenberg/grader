#Contestador de celular
numero=input("numero")
hora=input("hora")
hora=int(hora)
if hora>7 and hora<14:
  print("CONTESTAR")
elif hora>7 and hora<14:
  if numero[5:8]=="909":
    print("CONTESTAR")
elif hora>17 and hora<19:
  if numero[0:2]=="877":
    print("NO CONTESTAR")
  else:
    print("NO CONTESTAR")
else:
  print("NO CONTESTAR")