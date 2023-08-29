#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))
contestar = ""

if hora_llamada >= 0 and hora_llamada <= 7:
    contestar = "CONTESTAR"
elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
    contestar = "CONTESTAR"
elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico).startswith("877"):
    contestar = "NO CONTESTAR"
else:
    contestar = "NO CONTESTAR"
print("Resultado:", contestar)    