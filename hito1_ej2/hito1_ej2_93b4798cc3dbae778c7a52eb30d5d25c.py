numero_str=input("Numero de llamada:")
numero_int=int(numero_str)
hora=int(input("Hora de la llamada:"))


def numero():
  if len(numero_str)!=8:
    print("Error")
numero()

if hora>=0 and hora<=7:
  print("CONTESTAR")

if hora<=14 and hora>7 and numero_str[-3:]=="909":
  print("CONTESTAR")

if hora<=14 and hora>7 and numero_str[-3:]!="909":
  print("NO CONTESTAR")

if hora>14 and hora<17:
  print("NO CONTESTAR")

if hora>=17 and hora<=19 and numero_str[:3]!="877":
  print("CONTESTAR")

if hora>=17 and hora<=19 and numero_str[:3]=="877":
  print("NO CONTESTAR")

if hora>=19 and hora<=24:
  print("NO CONTESTAR")