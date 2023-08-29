#Ordenar tres números
##Entrada
num1=int(input("Digite el primero numero: "))
num2=int(input("Digite el segundo numero: "))
num3=int(input("Digite el tercer numero: "))
##Proceso
if num1 < num2 < num3:
  print(num1,num2,num3)
elif num1 < num3 < num2:
  print(num1,num3,num2)
elif num2 < num1 < num3:
  print(num2,num1,num3)
elif num2 < num3 < num1:
  print(num2,num3,num1)
elif num3 < num2 < num1:
  print(num3,num2,num1)
elif num3 < num1 < num2:
  print(num3,num1,num2 )
else:
  print("Digito mal un numero, reinicie el programa.")    