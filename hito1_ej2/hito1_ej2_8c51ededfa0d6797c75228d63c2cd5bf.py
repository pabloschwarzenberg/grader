numero=1000000000000
while(numero>99999999):
  numero=int(input("coloque un numero de telefono: "))
  hora=25
while(hora<=0 or hora>24):
 hora=int(input("coloque una hora: "))
if(hora>=0 and hora<=7):
  print("CONTESTAR")
elif(hora<14 and (numero%1000)!=909):
  print("NO CONTESTAR")
elif(hora<=19 and hora>=17 and (numero//100000)!=877):
  print("CONTESTAR") 
elif(hora<=19 and hora>=17):
  print("NO CONTESTAR")
elif(hora>=19):
  print("NO CONTESTAR")
else:
  print("CONTESTAR")