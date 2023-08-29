#Contestador de celular
numero = int(input("numero: "))
while not(numero>=10000000 and numero <=99999999):
  numero = int(input("ERROR....Ingrese numero de 8 digitos: "))

hora = int(input("Ingrese la hora [0-23]: "))
while not(hora>=0 and hora<=23):
   hora = int(input("ERROR....Ingrese la hora [0-23]: "))
   
#Desde aqui en adelante se ejecutan las instrucciones para numeros validos
primeros= numero//100000       #12345678//100000
ultimos= numero%1000
if (hora >=0 and hora <=7):
    print ("Contestar")
if(hora >=17 and hora <=19):
    if(numero//100000 == 877):
        print("No contestar")
    else:
        print ("Contestar")
if (hora <14):
    if(numero%1000==909):
        print("Contestar")
    else:
        print("No contestar")
if (hora >19):
    print("No contestar")  