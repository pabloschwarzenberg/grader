#Contestador de celular
num=int(input())
hr=int(input())
centena=num%1000
primeros=num//100000
if 0<hr<7:
  print("CONTESTAR")
elif hr<14:
  if centena==909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hr<19:
  if 17<hr<19:
    if primeros==877:
      print("NO CONTESTAR")
    else:
      print("CONTESTAR")
  else:
    print("NO CONTESTAR")
else:
  print("NO CONTESTAR")