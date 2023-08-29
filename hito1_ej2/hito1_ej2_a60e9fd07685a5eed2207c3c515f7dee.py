#Contestador de celular
num = input("Ingrese numero telefonico")
num_list = list(num)
hora = int(input("ingrese hora de la llamada: "))

if (0<=hora<=7):
  print("CONTESTAR")
elif (7<=hora<=14):
  if (num_list[5]=="9" and num_list[7]=="9" and num_list[6]=="0"):
    print("CONTESTAR")
  else:
    print("NO CONTESTAS")
elif (14<=hora<=19):
  if (num_list[0]==8 and num_list[1]==7 and num_list[2]==7):
    print("CONTESTAS")
  else:
    print("NO CONTESTAR")
else:
  print("NO CONTESTAR")     