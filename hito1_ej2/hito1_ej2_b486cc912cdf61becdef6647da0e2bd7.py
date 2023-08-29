#Contestador de celular
n=int(input("Ingrese numero de 8 digitos:"))
hora=int(input("Ingrese hora:"))
n=str(n)
if hora>=0 and hora<=7:
  print("contestar")
elif hora<14 and n[5:8]=="909":
  print("contestar")
elif hora>=17 and hora<=19 and n[0:3]!="877":
  print("contestar")
else:
  print("No contestar")