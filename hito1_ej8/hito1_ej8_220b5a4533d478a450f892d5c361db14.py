#Descomponer un número
v=int(input("Ingresa un valor: (máx 4 cifras) "))
M=(v//1000)
C=(v//100)%10
D=(v//10)%10
U=(v//1)%10
str1=M
str2=C
str3=D
str4=U
print(str1,"M +",+str2,"C +",+str3,"D +",+str4,"U")

      