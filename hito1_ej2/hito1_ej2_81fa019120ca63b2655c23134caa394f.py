#Contestador de celular
numero= int(input("ingrese numero de telefono: "))
while not (numero>=1000000 and numero<=99999999):
  numero= int(input("error este numero no es de ocho digitos: "))
  
hora= int(input("ingrese la hora (0-23): "))
while not (hora>=0 and hora<=23):
  hora= int(input("error ingrese la hora (0-23): "))

#desde aqui en adelante se ejecutan las instrucciones para numeros válidos
primerostres= numero//100000                  
ultimostres= numero%1000
print(primerostres)
print(ultimostres)

if(hora>=0 and hora<=7):
  print ("Contestar")

if(hora>=17 and hora<=19):
  print("No contestar")
else:
  print ("Contestar")

if(hora<14):
  print("Contestar")
else:
  print("No contestar")

if(hora >19):
  print("No contestar")