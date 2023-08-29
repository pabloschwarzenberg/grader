#Contestador de celular
num = ""
hora = -1
while len(num)!=8:
  num = int(input("ingrese numero telefonico:"))
  num = str(num)
while hora < 0 or hora > 23:
  hora = int(input("ingrese hora de la llamada:"))
if hora < 7:
  print("Resultado: CONTESTAR")
elif hora < 14 and num.endswith("909") == True:
  print("Resultado: CONTESTAR")
elif hora < 14:
  print("Resultado: NO CONTESTAR")
elif hora > 17 and hora < 19:
  print("Resultado: NO CONTESTAR")
elif hora > 17 and hora < 19 and num.endswith("877") == True:
  print("Resultado: NO CONTESTAR")
elif hora > 19:
  print("Resultado: NO CONTESTAR")