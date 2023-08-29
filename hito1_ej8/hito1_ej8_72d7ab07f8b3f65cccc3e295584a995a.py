#Descomponer un número
num=int(input("introduce un numero entero: "))
#unidad
num1= num % 10
#decena
num2= num //10 % 10
#centena
num3= num //100 % 10
#mil
num4= num //1000 % 10

num5= num //10000 % 10
num6= num //100000 % 10
num7= num //1000000 % 10
num8= num //10000000 % 10
num9= num //100000000 % 10
num0= num //1000000000 % 10


print(num4,"M+",num3,"C+",num2,"D+",num1,"U")
      