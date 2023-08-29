#Contestador de celular
numero=int(input())
hora=int(input())

if(0<hora<7):
  print("CONTESTAR")
if(7<hora<14):
  if(int(numero%1000==909)):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if(17<hora<19):
  if(numero//100000==877):
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if(19<hora):
  print("NO CONTESTAR")