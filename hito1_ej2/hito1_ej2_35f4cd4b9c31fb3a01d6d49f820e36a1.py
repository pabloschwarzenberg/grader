#Contestador de celular
num = str(input("Ingrese numero telefonico:"))
h = int(input("Ingrese hora de la llamada:"))

if h > 0 and h < 7:
  print("CONTESTAR")
if h > 19 and h <= 23:
  print("NO CONTESTAR")

else:
  if h > 7 and h < 14 and str(num[-3]) == "9" and str(num[-2]) == "0" and str(num[-1]) == "9":
    print("CONTESTAR")
  if h > 7 and h < 14 and str(num[-3]) != "9" and str(num[-2]) != "0" and str(num[-1]) != "9":
    print("NO CONTESTAR")
  if h > 17 and h < 19 and str(num[0:1]) == "8" and str(num[1:2]) == "7" and str(num[2:3]) == "7":
    print("NO CONTESTAR")
  if h > 17 and h < 19 and str(num[0:1]) != "8" and str(num[1:2]) != "7" and str(num[2:3]) != "7":
    print("CONTESTAR")      