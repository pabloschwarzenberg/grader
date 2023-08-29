#Contestador de celular
num = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora < 7:
  resultado = "CONTESTAR"
elif hora < 14:
  if num [-3:] == "909":
    resultado = "CONTESTAR"
  else:
    resultado = "NO CONTESTAR"
elif hora >= 17 and hora < 19:
  if num [:3] == "877":
    resultado = "NO CONTESTAR"
  else:
    resultado = "CONTESTAR"
else:
  resultado = "NO CONTESTAR"
print("Resultado:", resultado)