#Contestador de celular
#Entrada de datos
nroTelefonico = int(input("Ingrese numero telefonico: "))
horaLlamada = int(input("Ingrese hora de la llamada: "))

#Procesamiento de datos
if 0 <= horaLlamada >= 7:
    resultado = "CONTESTAR"
if horaLlamada < 14 and (nroTelefonico%1000 != 909):
    resultado = "NO CONTESTAR"
if horaLlamada < 14 and (nroTelefonico%1000 == 909):
    resultado = "CONTESTAR"
if 14 < horaLlamada > 17:
    resultado = "NO CONTESTAR"
if 17 <= horaLlamada >= 19 and (nroTelefonico//100000 == 877):
    resultado = "NO CONTESTAR"
if 17 <= horaLlamada >= 19 and (nroTelefonico//100000 != 877):
    resultado = " CONTESTAR"
if 19 < horaLlamada:
    resultado = "NO CONTESTAR"

#Salida de datos
print("Ingrese numero telefonico:", nroTelefonico)
print("Ingrese hora de la llamada:", horaLlamada)
print("Resultado:", resultado)