#Contestador de celular
FONO=int(input("ingrese número : "))
HORA=int(input("ingrese hora llamada: "))
NUM=FONO % 1000
if(0<=HORA<=7): print("CONTESTAR")

if(7<HORA<=14) and (NUM == 909):
   print("CONTESTAR")
else: 
  print("NO CONTESTAR")
if(17<=HORA<19) and (87700000<=FONO<=87799999): print("CONTESTAR")
if(HORA>=19): print("NO CONTESTAR")    