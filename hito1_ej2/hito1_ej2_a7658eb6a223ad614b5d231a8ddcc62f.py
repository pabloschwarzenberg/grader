#Contestador de celular
numero = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada: "))

if (0<=hora<=7):
  print("Resultado: CONTESTAR")
  
elif (0<=hora<=14) and (numero[5:7]!=909):
  print("Resultado: CONTESTAR")

elif (17<=hora<=19) and (numero[0:2]==877):
  print("Resultado: CONTESTAR")

else:
  print("Resultado: NO CONTESTAR")  
