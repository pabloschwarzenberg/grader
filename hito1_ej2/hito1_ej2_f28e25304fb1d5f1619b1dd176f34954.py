#Contestador de celular
numero_telefonico = int(input("Ingrese el número telefónico: "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))
if hora_llamada >= 0 and hora_llamada <= 7:
    respuesta = "NO CONTESTAR" 
elif hora_llamada < 14 and numero_telefonico % 100 == 909:
    respuesta = "CONTESTAR" 
elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico).startswith("877"):
    respuesta = "CONTESTAR"  
else:
    respuesta = "NO CONTESTAR"  
print("Resultado:", respuesta)
