#Contestador de celular
numero = int(input("Ingrese número de 8 cifras: "))    #12345678//1000
while not (numero>=10000000 and numero<=99999999):
  numero = int(input("ERROR.... Ingrese número de 8 cifras: "))

hora = int(input("Ingrese la Hora [0 - 23]: "))
while not (hora>=0 and hora<=23):
  numero = int(input("ERROR..... Ingrese la Hora [0 - 23]: "))

ultimostres = numero%1000
primerostres = numero//100000
if (hora<14):
  if(hora<=7 or ultimostres==909):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
else: #hora>=14
  if(hora>=17 and hora<=19):
    if(primerostres==877):
       print("NO CONTESTAR")
    else:
       print("CONTESTAR")
  else:
      print("NO CONTESTAR")

       
       