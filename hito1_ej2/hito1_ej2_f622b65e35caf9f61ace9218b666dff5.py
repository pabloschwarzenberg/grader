#Contestador de celular
n = int(input())
hora = int(input())
if hora < 7:
  print("CONTESTAR")
elif hora>=7 and hora<14:
  if n%1000==909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hora>=14 and hora<17:
  print("NO CONTESTAR")
elif hora >=17 and hora <19:
  if n//100000==877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
else:
  print("NO CONTESTAR")