#Contestador de celular
lista= []
numero = input("Ingrese numero telefonico: ")
numi = numero[:3]
numi = int(numi)

numf = numero[5:]
numf = int(numf)

hora = int(input("Ingrese hora de la llamada: "))

if 0 < hora < 7:
  print("CONTESTAR")

elif hora < 14 and numf == 909:
  print("CONTESTAR")

elif 17 < hora < 19 and numi != 877:
  print("CONTESTAR")

elif hora > 19:
  print("NO CONTESTAR")

else:
  print("NO CONTESTAR")
