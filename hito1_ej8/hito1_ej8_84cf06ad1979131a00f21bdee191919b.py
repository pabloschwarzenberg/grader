N=int(input("Ingresa una cifra de hasta 4 digitos: "))
M=(N//1000)
C=(N//100)%10
D=(N//10)%10
U=(N//1)%10
str1=M
str2=C
str3=D
str4=U
print(str1,"M +",+str2,"C +",+str3,"D +",+str4,"U")