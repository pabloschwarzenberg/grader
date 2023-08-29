#Contestador de celular
numerot=input()
hora=int(input())
l=numerot[5:]
k=int(l)
n=numerot[:3]
m=int(n)
if(0<hora<7):
  print("CONTESTAR")
if(7<hora<14):
  if(k==909):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if(17<hora<19):
  if(m==877):
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if(19<hora<23):
  print("NO CONTESTAR")

  
  