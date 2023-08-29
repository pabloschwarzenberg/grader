#Contestador de celular
#contestadora segun hora
numero = str(input("ingrese el numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))

x = numero[0:3]
y = numero[5:8]

if 0 <= hora <= 7:
  print("CONTSESTAR")

elif 7< hora <= 14:
  if y == "909":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")

elif 17 <= hora <= 19:
  if x == "877":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")

else: 
  print("NO CONTESTAR")   