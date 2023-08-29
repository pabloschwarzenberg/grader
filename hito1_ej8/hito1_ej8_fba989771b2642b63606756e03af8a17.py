#Descomponer un número
n=int(input("ingrese un numero de 4 digitos "))
U=n//1%10
D=n//10%10
C=n//100%10
M=n//1000%10
print(M,"M+",C,"C+",D,"D+",U,"U")