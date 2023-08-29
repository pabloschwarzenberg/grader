#Contestador de celular
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

contestar = False

if hora_llamada >= 0 and hora_llamada < 7:
    contestar = True
elif hora_llamada < 14:
    if str(numero_telefonico)[-3:] == "909":
        contestar = True
elif hora_llamada >= 17 and hora_llamada < 19:
    if not str(numero_telefonico).startswith("877"):
        contestar = True

if hora_llamada >= 19:
    contestar = False

if contestar:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
      