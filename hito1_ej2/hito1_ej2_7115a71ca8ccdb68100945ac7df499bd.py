#Contestador de celular
# Datos
NC_INT = int((input("Ingrese número de celular de 8 dígitos: ")))
HL = int((input("Ingrese hora de llamada: ")))
NC = str(NC_INT)

# Procesamiento
len(NC)
if (HL >= 0 and HL <= 7):
  print("CONTESTADO")
elif (HL < 14 and "909" in NC[5:8]):
  print("CONTESTAR")
elif (HL < 14):
  print("NO CONTESTAR")
elif (HL >= 17 and HL <= 19 and "877" in NC[0:3]):
  print("NO CONTESTAR")
elif (HL >= 17 and HL <= 19):
  print("CONTESTADO")
elif (HL > 19):
  print("NO CONTESTAR")
else:     
  print()