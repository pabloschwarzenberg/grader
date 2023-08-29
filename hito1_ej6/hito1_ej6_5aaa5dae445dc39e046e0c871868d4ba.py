#Ordenar tres números
num1 = int(input("Dame un numero:"))
num2 = int(input("Dame otro numero:"))
num3 = int(input("Dame otro otro numero:"))

if (num1 <= num2 <= num3):
  print("El orden de menor a mayor es:",num1, ",",num2,",",num3)
elif (num1 <= num3 <= num2):
  print("El orden de menor a mayor es:",num1, ",",num3,",",num2)
elif (num2 <= num1 <= num3):
  print("El orden de menor a mayor es:",num2, ",",num1,",",num3)
elif (num2 <= num3 <= num1):
  print("El orden de menor a mayor es:",num2, ",",num3,",",num1)
elif (num3 <= num2 <= num1):
  print("El orden de menor a mayor es:",num3, ",",num2,",",num1)
elif (num3 <= num1 <= num2):
  print("El orden de menor a mayor es:",num3, ",",num1,",",num2)
else:
  print("Relleno")