#Contestador de celular
n=int(input("ingrese numero: "))
hora=int(input("ingrese hora: "))
n=str(n)
if hora>=0 and hora<=7:
  print("Contestar")
elif hora<14 and n[5:8] == "909":
  print("Contestar")
elif hora>=17 and hora<=19 and n[0:3]!="877":
  print("Contestar")
else:
  print("No contestar")      