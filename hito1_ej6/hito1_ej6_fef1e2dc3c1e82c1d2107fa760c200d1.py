num1=int(input("Ingresa el primer numero"  ))
num2=int(input("Ingresa el segundo numero"  ))
num3=int(input("Ingresa el tercer numero"  ))

if num1 == num2 == num3:
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:",num3 +",",num2+",",num1)
elif (num2 >num1) and (num2 > num3) and (num1 == num3):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num3+",",num1+",",num2)

elif (num1 >num2) and (num1 > num3) and (num2 == num3):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num3 +",",num2+",",num1)

elif (num3 >num2) and (num3 > num1) and (num1 == num2):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num3 +",",num2+",",num1)

elif (num1 >num2) and (num1 > num3) and (num2 > num3):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num3 +",",num2+",",num1)

elif (num1 >num2) and (num1 > num3) and (num3 > num2):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num2 +",",num3+",",num1)

elif (num2 >num1) and (num2 > num3) and (num1 > num3):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num3 +",",num1+",",num2)

elif (num2 >num3) and (num2 > num1) and (num3 > num1):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num1 +",",num3+",",num2)

elif (num3 >num2) and (num3 > num1) and (num2 > num1):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num1 +",",num2+",",num3)

elif (num3 >num2) and (num3 > num1) and (num1 > num2):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num2 + ",",num1+",",num3)
  
  
  
elif (num2 < num1) and (num2 < num3) and (num1 == num3):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num2+",",num1+",",num3)
elif (num1 <num2) and (num1 < num3) and (num2 == num3):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num1+",",num2+",",num3)
elif (num3 <num1) and (num3 < num2) and (num1 == num2):
  num1=str(num1)
  num2=str(num2)
  num3=str(num3)
  print("El orden es:" ,num3+",",num1+",",num2)
  