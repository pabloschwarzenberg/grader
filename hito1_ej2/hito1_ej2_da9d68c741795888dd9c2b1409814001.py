NT = str(input("ingrese el numero telefonico: "))
Hrs = int(input("ingrese hora de la llamada: "))

PD = NT[0:3]
UD = NT[5:8]

if 0 <= Hrs <= 7:
  print("CONTSESTAR")

elif 7< Hrs <= 14:
  if UD == "909":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")

elif 17 <= Hrs <= 19:
  if PD == "877":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")

else: 
  print("NO CONTESTAR")