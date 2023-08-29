n=int(input("Ingrese el numero telefónico:"))
h=int(input("Ingrese la hora de llamada:"))
if h>=0 and h<=7:
  print("CONTESTAR")
elif h>7 and h<14:
  if (n-909)%1000==0:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif h>=14 and h<17:
  print("NO CONTESTAR")
elif h>=17 and h<=19:
  k=n-87700000
  if k>0 and k<100000:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
else:
  print("NO CONTESTAR")