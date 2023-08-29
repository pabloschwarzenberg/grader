#Contestador de celular
N = input("ingrese el numero telefonico: ")
H = int(input("ingrese hora de la llamada: "))

PD = N[0:3]
UD = N[5:8]

if 0 <= H <= 7:
  print("CONTSESTAR")

elif 7< H <= 14:
  if UD == "909":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")

elif 17 <= H <= 19:
  if PD == "877":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")

else: 
  print("NO CONTESTAR")