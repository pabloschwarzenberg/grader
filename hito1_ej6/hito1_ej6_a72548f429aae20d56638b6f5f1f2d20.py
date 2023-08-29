num1 = eval(input("ingrese un numero"))
num2 = eval(input("ingrese un segundo numero"))
num3 = eval(input("ingrese un tercer numero"))

if (num1 < num2 and num2 < num3):
  print(num1,",",num2,",",num3)
elif(num1 < num2 and num3 < num2):
  print(num1,",",num3,",",num2)
elif(num2 < num1 and num1 < num3):
  print(num2,",",num1,",",num3)
elif(num2 < num1 and num3 < num1):
  print(num2,",",num3,",",num1)
elif(num3< num1 and num1 < num2):
  print(num3,",",num1,",",num2)
elif(num3 < num1 and num2 < num1):
  print(num3,",",num2,",",num1)