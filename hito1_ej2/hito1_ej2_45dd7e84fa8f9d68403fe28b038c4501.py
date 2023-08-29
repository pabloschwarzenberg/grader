#Contestador de celular
#NT=NUMERO TELEFONO HR=HORA LLAMADA
NT=int(input("ingrese número del celular de 8 cifras "))
HR=int(input("ingrese hora de la llamada (0 a 23 hrs) "))
dig=NT % 1000
if(0<=HR<=7): print("CONTESTAR")

if(7<HR<=14) and (dig == 909):
   print("CONTESTAR")
else: 
  print("NO CONTESTAR")
if(17<=HR<19) and (87700000<=NT<=87799999): print("CONTESTAR")
if(HR>=19): print("NO CONTESTAR")