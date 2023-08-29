numero = int(input("Ingrese el Número de Teléfono: "))

hora = int(input("Ingrese la Hora de la Llamada: "))

salida = "no contestar"

str_numero = str(numero)

str_hora = str(hora)

inicio_numero = str_numero [0:3]

final_numero = str_numero [5:8]

if hora > 0 and hora < 7:
  con_cero = 1
  salida = "contestar"

if hora >= 7  and hora <= 14 and final_numero == "909":
  con_uno = 1
  salida = "contestar"
  
if hora >= 17  and hora <= 19 and inicio_numero != "877":
  con_dos = 1
  salida = "contestar"

if hora >= 19  and hora <= 23 :
  con_tres = 1
  salida = "no contestar"


print (salida)
