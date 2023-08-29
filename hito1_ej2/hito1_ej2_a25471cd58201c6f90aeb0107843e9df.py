#Contestador de celular
num =(input("Ingrese numero telefonico: "))

hora = int(input("Ingrese hora de la llamda: "))

ultnum = num[-3:]
primnum = num[:3]

if (hora > 0 and hora <= 7):
   print("Contestar")  

elif (hora > 7 and hora < 14 ):
   if ultnum == "909":
       print("Contestar")
   else:
       print("No contestar")
elif (hora > 17 and hora < 19):
   if primnum == "877":
       print("No contestar")
   else:
       print("Contestar")
elif (hora > 19):
     print("No contestar")       