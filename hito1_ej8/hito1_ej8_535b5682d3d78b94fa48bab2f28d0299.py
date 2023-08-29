a=int(input("Ingresar numero a descomponer: "))
M=a//1000
C=(a//100)%10
D=(a//10)%10
U=a%10

print(M,"M +",C,"C +",D,"D +",U,"U")