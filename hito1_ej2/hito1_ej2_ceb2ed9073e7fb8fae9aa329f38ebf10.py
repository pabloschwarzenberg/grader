#Contestador de celular
#Contestador de celular
nt = int(input("Numero telefonico :"))
hdl = int(input("Hora de llamada :"))
nt = str(nt)

if hdl >= 0 and hdl <= 7 :
  print("Contestar") 
elif hdl < 14 and nt[-3:] == "909" :
  print("Contestar")
elif hdl < 14 :
  print("No contestar")
elif hdl >= 17 and hdl <= 19 and nt[0:3] == "877" :
  print("No contestar")
elif hdl >= 17 and hdl <= 19 :
  print("Contestar")
elif hdl > 19 :
  print("No contestar")