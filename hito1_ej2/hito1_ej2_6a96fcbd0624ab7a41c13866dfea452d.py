#Contestador de celular
num_telefono = input("Ingrese un número telefónico de 8 cifras")
hora_llamada = int(input("Ingrese la hora de la llamada"))

def contestar(numero, hora):
  numero_empieza_877 = numero[0:3] == "877"
  numero_termina_909 = numero[-3:] == "909"
  
  if hora <= 7: return True
  if 7 < hora < 14 and numero_termina_909: return True
  if 7 < hora < 14 and not numero_termina_909: return False
  if 14 <= hora < 17: return False
  if 17 <= hora <= 19 and not numero_empieza_877: return True
  if 17 <= hora <= 19 and numero_empieza_877: return False
  if hora > 19: return False
  
if contestar(num_telefono, hora_llamada):
   print("CONTESTAR")
else: print("NO CONTESTAR")