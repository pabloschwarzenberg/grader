#Contestador de celular
n = input("Ingrese el numero ")
h = int(input("Ingrese la hora "))
if 7 < h < 14 and n[-1] == "9" and n[-2] == "0" and n[-3] == "9":
  print("CONTESTAR")
elif 17 <= h <= 19 and n[0] == "8" and n[1] == "7" and n[2] == "7":
  print("NO CONTESTAR")
elif 17 <= h <= 19:
  print("CONTESTAR")
elif 0 <= h <= 7:
  print("CONTESTAR")
elif h > 19 :
  print("NO CONTESTAR")
elif 7 < h < 14: 
  print("NO CONTESTAR")
      