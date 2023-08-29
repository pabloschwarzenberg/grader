#Ordenar tres números
num1=int(input("Ingrese el primer numero "))
num2=int(input("Ingrese el segundo numero "))
num3=int(input("Ingrese el tercer numero "))
if(num1>=num2):
  auxiliar=num1
  num1=num2
  num2=auxiliar
if(num1>=num3):
  auxiliar=num1
  num1=num3
  num3=auxiliar
if(num2>=num3):
  auxiliar=num2
  num2=num3
  num3=auxiliar
print(num1,num2,num3)
