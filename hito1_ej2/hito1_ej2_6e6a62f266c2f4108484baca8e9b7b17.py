n1=int(input("ingrese su numero telefonico: "))
n2=int(input("ingrese la hora de la llamada: "))
celular= str(n1)
l1 = celular[0:3]
l2 = celular[5:8]
if (n2 >= 17) and (n2<= 19) and (l1 != "877"):
  print("CONTESTAR")
elif (n2 >= 17) and (n2<= 19) and (l1 == "877"):
  print("NO CONTESTAR")
elif(n2 >= 0) and (n2<= 7):
  print("CONTESTAR 3")
elif(n2 <= 14) and (l2!="909"):
  print("NO CONTESTAR 4" )
elif (n2 <= 14) and (l2 == "909"):
  print("CONTESTAR 5")
else: 
  print("NO CONTESTAR 6 ")
