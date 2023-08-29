#Descomponer un número

n=int(input("ingrese numero"))

if len(str(n))== 4:

  m=int((str(n)[0]))
  c=int((str(n)[1]))
  d=int((str(n)[2]))
  u=int((str(n)[3]))
  print (m,"M + ", c,"C + ", d, "D + ", u, "U")

elif len(str(n))== 3:

  c=int((str(n)[0]))
  d=int((str(n)[1]))
  u=int((str(n)[2]))
  print (c,"C + ", d, "D + ", u, "U")
  
elif len(str(n))== 2:

  d=int((str(n)[0]))
  u=int((str(n)[1]))
  print (d, "D + ", u, "U")
  
elif len(str(n))== 1:
  
  u=n
  print (u, "U")