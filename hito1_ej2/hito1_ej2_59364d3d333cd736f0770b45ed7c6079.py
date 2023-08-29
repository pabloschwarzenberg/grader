numero=input("Numero: ")
hora=int(input("Hora: "))
if hora<=7 and hora>=0:
   print("CONTESTAR")
if hora>19:
  print("NO CONTESTAR")
if hora==15 or hora==16:
  print("NO CONTESTAR")
if hora>7 and hora<=13:
  if numero[5:8]=="909":
   print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if hora>=17 and hora<19:
  if numero[5:8]=="877":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")  