num1=int(input("Ingrese el número 1: "))
num2=int(input("Ingrese el número 2: "))
num3=int(input("Ingrese el número 3: "))
if num1>=num2>=num3:
  print((num3, num2, num1))
elif num1>=num3>=num2:
  print((num2, num3, num1))
elif num2>=num1>=num3:
  print((num3, num1, num2))
elif num2>=num3>=num1:
  print((num1, num3, num2))
elif num3>=num1>=num2:
  print((num2, num1, num3))
elif num3>=num2>=num1:
  print((num1, num2, num3))