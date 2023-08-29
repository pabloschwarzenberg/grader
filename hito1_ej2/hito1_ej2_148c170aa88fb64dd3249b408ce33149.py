#Contestador de celular
llamada=int(input("Ingrese su numero telefonico de ocho digitos: "))
hora=int(input("Ingrese hora de la llamada: "))
if(0<=hora and hora<=7):
  print("Contestar por Emergencia")
if (llamada % 1000 == 909) and (hora>=8 and hora<=14):
     print("contestar")
if (llamada % 1000 != 909) and (hora>=8 and hora<=14):
     print("No contestar")
elif(llamada % 100000000 // 1000000 == 877) and (hora>=17 and hora<=19):
  print("Contestar")
elif(llamada % 100000000 // 1000000 != 877) and (17<=hora and hora<=19): 
   print("No Contestar") 
if (hora>=19 and hora<=23):
  print("no Contestar")