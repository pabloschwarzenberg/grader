#Contestador de celular
nro=int(input())
hora=int(input())
nros=str(nro)
if 0<=hora<=7:
  print("CONTESTAR")
if 7<hora<=14:
  if nros[7]=="9" and nros[6]=="0" and nros[5]=="9":
   print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if 14<=hora<=19:
  if nros[0]=="8" and nros[1]=="7" and nros[2]=="7":
   print(" NO CONTESTAR")
  else:
    print("CONTESTAR")
if 19<=hora:
  print("NO CONTESTAR")
 