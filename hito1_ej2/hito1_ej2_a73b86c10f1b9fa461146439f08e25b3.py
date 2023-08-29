#Contestador de celular
fono= int(input("Numero telefonico: "))
hora = int(input("Hora de llamada: "))
ent = fono//100000
ter = fono % 1000
if hora == 0 or hora == 1 or hora == 2 or hora == 3 or hora == 4 or hora == 5 or hora == 6 or hora == 7:
  print("CONTESTAR")
if hora in range(8,14) and ter == 909:
  print("CONTESTAR")
if hora in range(17,19) and ent == 877:
  print("NO CONTESTAR")
if hora in range(19,0):
  print("NO CONTESTAR")
if hora == 15 or hora == 16: 
  print("NO CONESTAR")
if hora == 20 or hora == 21 or hora == 22 or hora == 23:
  print("NO CONTESTAR")
