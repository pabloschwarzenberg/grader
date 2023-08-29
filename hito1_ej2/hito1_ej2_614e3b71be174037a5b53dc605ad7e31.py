#Contestador de celular
numeroTelefono=0
while (numeroTelefono<10000000 or numeroTelefono>99999999):
  numeroTelefono=int(input("Numero de telefono: "))
hora=100
while (hora<0 or hora>23):
  hora=int(input("hora de llamada: "))

if ((numeroTelefono//100000==877) and (hora>=17 and hora<=19)):
  print("No contestar")

elif ((numeroTelefono>10000000 or numeroTelefono<99999999) and (hora>=0 and hora<7)): 
  print("contestar")

elif ((numeroTelefono%1000==909) and (hora>=0 and hora<14)):
  print("Contestar")

else:
  print("No contestar")