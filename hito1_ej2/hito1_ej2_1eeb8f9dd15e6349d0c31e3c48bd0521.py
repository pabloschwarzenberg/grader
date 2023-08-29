#Contestador de celular
numero = int(input("Ingrese número de 8 cifras: "))    
while not (numero>=10000000 and numero<=99999999):
  numero = int(input("Error, no ingresó un número de 8 cifras. Vuelva a ingresar el número: "))

hora = int(input("Ingrese la Hora [0 - 23]: "))
while not (hora>=0 and hora<=23):
  numero = int(input("Error, Inténtelo de nuevo por favor [0 - 23]: "))

ultimos = numero%1000
primeros = numero//100000
if (hora<14):
  if(hora<=7 or ultimos==909):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
else: 
  if(hora>=17 and hora<=19):
    if(primeros==877):
       print("NO CONTESTAR")
    else:
       print("CONTESTAR")
  else:
      print("NO CONTESTAR")
