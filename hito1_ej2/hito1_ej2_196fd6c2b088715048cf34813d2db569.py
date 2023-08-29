#Contestador de celular
numero = int(input("Numero: "))
hora = int(input("hora: "))
entrada = numero//100000
termina = numero % 1000
if hora == 0 or hora == 1 or hora == 2 or hora == 3 or hora == 4 or hora == 5 or hora == 6 or hora == 7:
  print("CONTESTAR")
elif hora in range(8,14) and termina == 909:
  print("CONTESTAR")
elif hora in range(17,19) and entrada == 877:
  print("NO CONTESTAR")
elif hora in range(19,0):
  print("NO CONTESTAR")
elif hora == 15 or hora == 16: 
  print("NO CONESTAR")
elif hora == 20 or hora == 21 or hora == 22 or hora == 23:
  print("NO CONTESTAR")   