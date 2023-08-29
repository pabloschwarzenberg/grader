#Contestador de celular

while True:
   strnumtel = input("Ingrese Número Telefónico: ")
   if len(strnumtel) == 8:
      break

numtel=int(strnumtel)

hora = int(input("Ingrese Hora de Llamada: "))

if hora >= 0 and hora <= 7:
   strRes = "Contestar"
elif hora <= 14:
   strRes = "No Contestar"
   if strnumtel[-3:] == "909":
      strRes = "Contestar"
elif hora >= 17 and hora <= 19:
   strRes = "Contestar"
   if strnumtel[:3] == "877":
      strRes = "No Contestar"
elif hora > 19:
   strRes = "No Contestar"

print("Resultado:", strRes)