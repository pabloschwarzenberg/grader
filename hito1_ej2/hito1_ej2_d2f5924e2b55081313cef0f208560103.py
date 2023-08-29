#Contestador de celular
n = input("cual es tu numero telefono?: ")
h = int(input("A que hora es tu llamada?: "))
if (0 <= h <= 7):
   print("contestar")
elif (n[5:] == "909" and h < 14):
     print("contestar")
elif (n[0:2] == "887" and 17 <= h <= 19):
     print("no contestar")
elif (h >19):
     print("no contestar")
else:
     print("no contestar")