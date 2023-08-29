numero=input()
hora=input()
if 0<=int(hora)<=7:
  print("CONTESTAR")
if 7<int(hora)<=14:
  if (int(numero)%1000)!=909:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if 14<int(hora)<17:
  print("NO CONTETAR")
if 17<=int(hora)<=19:
  if (int(numero)%1000)!=877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if 19<int(hora):
  print("NO CONTESTAR")

