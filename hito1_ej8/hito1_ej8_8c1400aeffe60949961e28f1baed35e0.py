#Descomponer un número
a=int(input())
M=a//1000
C=a//100-10*M
D=a//10-100*M-10*C
U=a-1000*M-100*C-10*D
if 1000<=a:
    print(M,"M+",C,"C+",D,"D+",U,"U")
if 100<=a<1000:
    print(C,"C+",D,"D+",U,"U")
if 10<=a<100:
    print(D,"D+",U,"U")
if 1<=a<10:
    print(U,"U")
      