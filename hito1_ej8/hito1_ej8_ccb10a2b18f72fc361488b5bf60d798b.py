#Descomponer un número
num = int(input("ingrese un numero de maximo 4 digitos: "))
m = num // 1000
c = num // 100 %10
d = num // 10 %10
u = num // 1 %10
str1= m
str2=c
str3=d
str4=u

print(str1,"M +",+str2,"C +",+str3,"D +",+str4,"U")     