#Contestador de celular
num = str(input("Ingrese el número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

e = num[0:3]
nc = num[5:8]

if 0 <= hora <= 7:
  print("CONTSESTAR")

elif 7 < hora <= 14:
  if nc == "909":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")

elif 17 <= hora <= 19:
  if e == "877":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")

else: 
  print("NO CONTESTAR")