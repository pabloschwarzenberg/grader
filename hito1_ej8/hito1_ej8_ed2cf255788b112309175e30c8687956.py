#Descomponer un número
num=int(input("ingrese un numero de 4 digitos"))
num1=num//1000
num2=(num-num1*1000)//100
num3=(num-(num1*1000+num2*100))//10
num4=num-(num1*1000+num2*100+num3*10)
print(num1,"M +",num2,"C +",num3,"D +",num4,"U")
