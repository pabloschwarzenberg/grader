num = input("Escribe un numero de maximo 4 digitos: ")
longitud = len(num)

if(longitud > 4):
  print("El numero tiene mas de 4 digitos intenta de nuevo.")

elif(longitud == 1):
  print(num,"U")

elif(longitud == 2):
  print(num[0],"D","+",num[1],"U")

elif(longitud == 3):
  print(num[0],"C","+",num[1],"D","+",num[2],"U")

elif(longitud == 4):
  print(num[0],"M","+",num[1],"C","+",num[2],"D","+",num[3],"U")