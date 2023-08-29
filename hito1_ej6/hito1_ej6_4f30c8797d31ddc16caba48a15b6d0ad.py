#Ordenar tres números
num1=int(input("coloque el primer numero: "))
num2=int(input("coloque el segundo numero: "))
num3=int(input("coloque el tercer numero: "))
if(num1<=num2<=num3):
    print("orden de menor a mayor es: ",',',num1,',',num2,',',num3)
if(num1<=num3<=num2):
    print("orden de menor a mayor es: ",',',num1,',',num3,',',num2)
if(num2<=num1<=num3):
    print("orden de menor a mayor es: ",',',num2,',',num1,',',num3)
if(num2<=num3<=num1):
    print("orden de menor a mayor es: ",',',num2,',',num3,',',num1)
if(num3<=num1<=num2):
    print("orden de menor a mayor es: ",',',num3,',',num1,',',num2)
if(num3<=num2<=num1):
   print("orden de menor a mayor es: ",',',num3,',',num2,',',num1)