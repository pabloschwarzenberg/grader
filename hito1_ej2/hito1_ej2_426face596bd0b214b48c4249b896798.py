#Contestador de celular

telefono = str(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de llamada: "))


if hora >= 0 and hora <= 7:
  resultado = "CONTESTAR"

elif hora < 14:
  if telefono[5:8] != "909":
    resultado = "NO CONTESTAR"
  else:
    resultado = "CONTESTAR"
        
elif hora >= 15 and hora < 17:
  resultado = "NO CONTESTAR"

elif hora >= 17 and hora <= 19:
  if telefono[0:3] != "877":
    resultado = "CONTESTAR"
  else:
    resultado = "NO CONTESTAR"

if hora > 19 and hora <= 23:
    resultado = "NO CONTESTAR"

print("Resultado: ", resultado)