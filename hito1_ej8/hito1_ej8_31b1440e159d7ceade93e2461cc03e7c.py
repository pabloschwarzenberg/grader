#Descomponer un número
n = int(input("numero: "))

M = n//1000
U = (n%10)
D = (n%100)//10
C = (n%1000)//100

print(M,"M","+",C,"C","+",D,"D","+",U,"U")