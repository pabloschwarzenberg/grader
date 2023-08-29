#Contestador de celular
a = int (input ("Ingrese Numero Telefonico: "))
numero = str(a) 
print (a)
b = int (input ("Ingrese Hora de Llamada: "))
print (b) 
if 0 < b and b < 7 :
  print ("CONTESTAR")
elif (7 <= b and b < 14) and numero[-3:] == "909":
  print ("CONTESTAR")
elif (14 <= b and b <= 15):
  print ("NO CONTESTAR")
elif (15 < b and b <= 19) and numero[0:2] == "877":
  print ("NO CONTESTAR") 
elif 19 < b and b < 23: 
  print ("NO CONTESTAR")
else:
  print("NO CONTESTAR")
    

