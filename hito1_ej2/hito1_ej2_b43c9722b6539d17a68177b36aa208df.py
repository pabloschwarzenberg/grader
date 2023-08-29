#Contestador de celular
numero=int(input("ingrese numero telefonico"))
hora=int(input("ingrese hora"))
num1= numero//1000000
num2= numero%1000
if hora>=0 and hora<=7:
  print("CONTESTAR")
elif hora>7 and hora<14 and num2==909:
  print ("CONTESTAR")
elif hora>17 and hora<19 and num1==877:
  print ("CONTESTAR")
else:
  print("NO CONTESTAR")