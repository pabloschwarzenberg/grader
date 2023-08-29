#Contestador de celular
n = input("cual es tu numero telefono?: ")
h = int(input("A que hora es tu llamada?: "))
if (0 <= h <= 7):
   print("CONTESTAR")
elif (n[5:] == "909" and h < 14):
     print("CONTESTAR")
elif (n[0:2] == "887" and 17 <= h <= 19):
     print("NO CONTESTAR")
elif (h >19):
     print("NO CONTESTAR")
else:
     print("NO CONTESTAR")      