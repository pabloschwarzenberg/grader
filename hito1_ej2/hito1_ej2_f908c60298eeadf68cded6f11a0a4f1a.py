X = str(input("ingrese el numero telefonico: "))
Y = int(input("ingrese hora de la llamada: "))

NT = X[0:3]
JJ = X[5:8]

if 0 <= Y <= 7:
  print("CONTSESTAR")

elif 7< Y <= 14:
  if JJ == "909":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")

elif 17 <= Y <= 19:
  if NT == "877":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")

else: 
  print("NO CONTESTAR")