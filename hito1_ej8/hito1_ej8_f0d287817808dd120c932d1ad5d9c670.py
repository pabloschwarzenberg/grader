#Descomponer un número
num = int(input("Introduzca Número: "))

M = num//1000
N = num%1000

C = N//100
N = N%100

D = N//10
U = N%10


if M == 0:
    print (C,"C +",D,"D +",U,"U")

elif M == 0 and C == 0:
    print (D,"D +",U,"U")

elif M == 0 and C == 0 and D == 0:
    print(U,"U")

else:
    print (M,"M +",C,"C +",D,"D +",U,"U")
      