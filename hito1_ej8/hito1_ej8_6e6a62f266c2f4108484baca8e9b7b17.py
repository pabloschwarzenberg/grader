#Descomponer un número
n1=int(input("ingresa un numero de 4 digitos: "))
numero_ingresado = str(n1)
l1 = numero_ingresado[0:1]
l2 = numero_ingresado[1:2]
l3 = numero_ingresado[2:3]
l4 = numero_ingresado[3:4]
if (n1 < 10000) and (n1 >= 1000):
  print(l1,"M","+", l2, "C","+", l3, "D","+", l4, "U")
elif(n1 < 1000) and (n1 >= 100):
  print(l1,"C","+", l2, "D","+", l3, "U")
elif(n1 < 100) and (n1 >= 10):
  print(l1,"D","+", l2, "U")
elif(n1 <= 10):
  print(l1,"U")
else:
  print(" tu numero no es valido ")