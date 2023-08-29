numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

contestar = False

if hora_llamada >= 0 and hora_llamada < 7:
    contestar = True
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    contestar = True
elif hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico // 10000000 == 877:
    contestar = True

if contestar:
    resultado = "CONTESTAR"
else:
    resultado = "NO CONTESTAR"

print("Resultado:", resultado)
      