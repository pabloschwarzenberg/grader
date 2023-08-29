#Descomponer un número
n= int(input("ingrese un numero de 4 digitos como maximo:"))
a=n//1000
b=n//100%10
c=n//10%10
d=n//1%10
str1=a
str2=b
str3=c
str4=d
print(str1,"M +",str2,"C +",str3,"D +",str4,"U +")