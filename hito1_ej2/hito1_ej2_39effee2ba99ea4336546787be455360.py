cel=input("Ingresa el numero celular 99999999 de 8 cifras: \n")
hora=int(input("a qué hora llama?:\n"))
nueve=0
ocho=0
if (cel[5:])==("909"):
  nueve=1
if (cel[0:3])==("877"):
  ocho=1
if hora>=0 and hora<=7:
  print("CONTESTAR")
if hora>7 and hora<=14:
  if nueve==1:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if hora>14 and hora<17:
  print("NO CONTESTAR")
if hora>=17 and hora<=19:
  if ocho==1:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if hora>19 and hora<=23:
  print("NO CONTESTAR")
  