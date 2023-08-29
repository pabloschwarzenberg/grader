#Contestador de celular
n_t = int(input("Ingrese numero telefonico: "))
h_l = int(input("Ingrese hora de la llamada: "))
n = str(n_t)
if 0 <= h_l <= 7:
  print("Resultado: CONTESTAR")
elif n[5:8] != '909' and 8 <= h_l <= 13:
  print("Resultado: NO CONTESTAR")
elif n[5:8] == '909' and  8 <= h_l <= 13:
  print("Resultado: CONTESTAR")
elif n[0:3] == '877' and 17 <= h_l <= 19:
  print("Resultado: NO CONTESTAR")
elif n[0:3] != '877' and 17 <= h_l <= 19:
  print("Resultado: CONTESTAR")
elif 20 <= h_l <= 23:
  print("Resultado: NO CONTESTAR")