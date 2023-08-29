#Contestador de celular

a = int(input("Ingrese numero telefonico: "))
b = int(input("Ingrese hora de la llamada: "))

if 0 <= b <= 7:
      print("CONTESTAR")

if 7 < b <= 14 and (a%1000 != 909):
      print("NO CONTESTAR")      
elif 7 < b <= 14 and (a%1000 == 909):
      print("CONTESTAR")

if 14 < b < 17:
      print("NO CONTESTAR")
      
if 17 <= b <= 19 and (a//100000 != 877):
      print("CONTESTAR")
elif 17 <= b <= 19 and (a//100000 == 877):
      print("NO CONTESTAR")

if 19 < b < 24:
      print("NO CONTESTAR")
