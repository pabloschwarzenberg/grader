#Contestador de celular
N=int(input("Ingrese número telefónico: "))
H=int(input("Ingrese hora de la llamada: "))
if H>=0 and H<=7:
  print("CONTESTAR")
elif H<=14 and N%1000==909:
  print("CONTESTAR")
elif (H>=17 and H<=19) and N//100000!=877:
  print("CONTESTAR")
elif H>=20 and H<=23:
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")