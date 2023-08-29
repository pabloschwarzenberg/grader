#Contestador de celular

NumLL=int(input("Ingrese número de Telefono: "))
Hora=int(input("Ingrese hora de la llamada"))
dig=NumLL % 1000
if(0<=Hora<=7): print("CONTESTAR")

if(7<Hora<=14) and (dig == 909):
   print("CONTESTAR")
else: 
  print("NO CONTESTAR")
if(17<=Hora<19) and (87700000<=NumLL<=87799999): print("CONTESTAR")
if(Hora>=19): print("NO CONTESTAR")
      