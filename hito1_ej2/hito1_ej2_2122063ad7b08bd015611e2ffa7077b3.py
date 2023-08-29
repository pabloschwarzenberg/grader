#Contestador de celular
nf=str(int(input("Ingrese numero de telefono ")))
h = int(input("Ingrese hora de la llamada "))
if 0 <= h <= 7:
  print("CONTESTAR")
if h <= 14 and nf[5] != "9" and nf[6] != "0" and nf[7] != "9":
  print("NO CONTESTAR")
if h <= 14 and nf[5] == "9" and nf[6] == "0" and nf[7] == "9":
  print("CONTESTAR")
if 17 <= h <= 19:
  print("NO CONTESTAR")
if 17 <= h <= 19 and nf[0] == "8" and nf[1] == "7" and nf[2] =="7":
  print("CONTESTAR")
if h > 19:
  print("NO CONTESTAR")