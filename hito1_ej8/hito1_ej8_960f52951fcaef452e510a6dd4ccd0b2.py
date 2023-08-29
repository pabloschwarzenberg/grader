#Descomponer un número
x = eval(input("Ingrese un numero de 4 digitos: "))
m = x // 1000
c = x // 100%10
d = x // 10%10
u = x // 1%10
str1 = m
str2 = c
str3 = d
str4 = u
print(str1,"M +" ,str2,"C +" ,str3,"D +" ,+str4,"U")