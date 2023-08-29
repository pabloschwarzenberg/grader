#Contestador de celular
numero = int(input("escriba su numero de celular\n"))
hora = int(input("mencione la hora\n"))
codigo1 = numero - ((numero // 10**3) * 10**3)
codigo2 = (numero // 10**5)

if 7 >= hora >= 0 :
  print("Contestar el llamado de emergencia")
while 7 < hora <= 14 :
  if codigo1 == 909 :
    print("Contestar")
    break  
  else :
    print("No contestar")
    break
while 17<= hora <= 19 :
    if codigo2 == 877 :
        print("No contestar")
        break
    else :
        print("Contestar")
        break 
if hora > 19 :
        print("No contestar")