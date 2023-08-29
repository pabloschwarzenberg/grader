numero_telefonico=int(input())
hora=int(input())
if 0 <= hora <= 7:
  print("CONTESTAR")
if 7 < hora < 14:
  if numero_telefonico-((numero_telefonico//1000)*1000)==909:
    print("CONTESTAR")
  else:
    print ("NO CONTESTAR")
if 17 <= hora <= 19:
  if numero_telefonico-(numero_telefonico%1000000)==877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if hora > 17:
  print("NO CONTESTAR")
      