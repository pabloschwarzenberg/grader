#Contestador de celular
n = int(input("Ingrese numero telefonico de 8 digitos(12345678):"))
h = int(input("Ingrese hora de la llamada(0 a 23):"))
last3 = int(str(n)[-3:])
first3 = int(str(n)[:3])

if (h >= 0 and h <= 7) or (h <= 14 and last3 == 909) or (h >= 17 and h <= 19 and first3 != 877):
  print("CONTESTAR")

elif (h < 14) or (h >= 17 and h <= 19 and first3 == 877) or (h > 19) :
  print("NO CONTESTAR")