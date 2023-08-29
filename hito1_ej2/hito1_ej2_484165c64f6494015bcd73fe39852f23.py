#Contestador de celular
tel = int(input("Ingrese el número telefónico al cual llama, 8 dígitos: "))
hora = int(input("Hora de la llamada: "))
if hora >= 0 and hora <= 7: 
  print("Contestar, puede ser una emergencia.")
if hora > 7 and hora <= 14:
  if tel%1000 == 909:
    print("Contestar.")
  else: 
    print("No Contestar")
if hora >= 17 and hora <= 19:
  if tel//100000 == 877:
    print("No contestar.")
  else:
    print("Contestar.")
if hora > 19:
  print("No contestar.") 
     