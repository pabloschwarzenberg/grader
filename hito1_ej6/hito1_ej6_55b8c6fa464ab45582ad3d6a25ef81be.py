#Ordenar tres números
num1=int(input("Ingrese numeros: "))
num2=int(input("Ingrese numeros: "))
num3=int(input("Ingrese numeros: "))
if(num3>=num2>=num1):
  print(num1,",", num2,",", num3)
elif(num3>=num1>=num2):
  print(num2,",", num1,",", num3)
elif(num2>=num3>=num1):
  print(num1,",", num3,",", num2)
elif(num2>=num1>=num3):
  print(num3,",", num1,",", num2)
elif(num1>=num2>=num3):
  print(num3,",", num2,",", num1)
elif(num1>=num3>=num2):
  print(num2,",", num3,",", num1)