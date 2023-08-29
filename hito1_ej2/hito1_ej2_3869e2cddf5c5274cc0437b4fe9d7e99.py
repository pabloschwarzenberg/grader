numero = int(input("mencione su numero de celular (8 digitos)\n"))
hora = int(input("mencione la hora (0 a 23)\n:"))
tiempo= hora
codigo1 = numero - ((numero // 10**3) * 10**3)
codigo2= (numero // 10**5 )

if 7 >= tiempo >= 0:
  print("Contestar el llamado de emergencia baby")
while 7 < tiempo < 14:
  if 909> codigo1 <909:
    print("no contestar")
    break 
  if codigo1 == 909:
    print ("contestar")
    break
while 17<= tiempo <= 19:
  if 877> codigo2 < 877:
   print("Contestar")
   break
  if codigo2 == 877:
   print("No contestar")
   break   
if tiempo > 19:
 print ("no contestar")