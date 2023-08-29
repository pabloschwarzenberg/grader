#Ordenar tres números

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el primer segundo: "))
num3 = int(input("Ingrese el primer tercer: "))

if (num1>=num2>=num3) or (num1>=num3>=num2):
  if (num2>=num3):
    print(num3,",",num2,",",num1)
  else:
    print(num2,",",num3,",",num1)
elif (num2>=num1>=num3) or (num2>=num3>=num1):
  if (num1>=num3):
    print(num3,",",num1,",",num2)
  else:
    print(num1,",",num3,",",num2)
elif (num3>=num1>=num2) or (num3>=num2>=num1):
  if (num1>=num2):
    print(num2,",",num1,",",num3)
  else:
    print(num1,",",num2,",",num3)

