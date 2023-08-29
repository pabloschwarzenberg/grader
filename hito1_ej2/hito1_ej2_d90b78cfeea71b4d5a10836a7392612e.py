#Contestador de celular
numero_telefonico = input("Ingrese número telefónico: ")

hora_llamada = int(input("Ingrese hora de la llamada: "))

while numero_telefonico.endswith("909"):
  print("CONTESTAR")
  break

  if hora_llamada <=  14:
    print("NO CONTESTAR")

while numero_telefonico.startswith("877"):
  print("NO CONTESTAR")
  break

  if hora_llamada >= 17 and hora_llamada <= 19:
    print("CONTESTAR")

if hora_llamada >= 0 and hora_llamada <= 7:
  print("CONTESTAR")

elif hora_llamada >= 19:
  print("NO CONTESTAR")
      