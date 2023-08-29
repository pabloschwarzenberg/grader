#Descomponer un número
a=int(input(""))
M=a//1000
C=((a//100)%10)
D=((a//10)%10)%10
U=((a%10)%10)%10
if M == 0:
  print(C,"C +",D,"D +",U,"U")
if M == 0 and C == 0:
  print(D,"D +",U,"U")
if M == 0 and C == 0 and D == 0:
  print(U,"U")
else:
  print(M,"M +",C,"C +",D,"D +",U,"U")