#Contestador de celular
num = int(input("Ingrese el número teléfonico:"))
validar_num = str(num)[5:8] 
hora = int(input("Ingrese la hora de la llamada:"))
if hora >= 0 and hora < 7:
  print("CONTESTAR")
elif hora >= 7 and hora < 14 and validar_num == "909":
  print("CONTESTAR")
elif hora >= 17 and hora < 19 and validar_num == "877":
  print("CONTESTAR")
else:
  print("NO CONTESTAR")