#Contestador de celular
N_numero=int(input("Ingrese el numero de telefono: "))
hora=int(input("Ingrese hora de llamada: "))
while (N_numero<9999999 and N_numero>99999999):
  print("Numero inválido")
  N_numero=int(input("Ingrese el numero de telefono: "))
if(hora>=0 and hora <=7):
  print("Contestar")
elif(hora<14 and N_numero%1000==909):
  print("Contestar")
elif(hora<14):
  print("No contestar")
elif(hora>=17 and hora<=19 and N_numero//1000>=877):
  print("No contestar")
elif(hora>=17 and hora <=19):
  print("Contestar")
elif(hora>19):
   print("No contestar")
  