#Descomponer un número
import math
cifra=int(input("ingrese a number de maximo 4 digitos:"))

if cifra <= 9999:
        M=math.trunc(cifra/1000)
        A=cifra-(M*1000)
        C=math.trunc(A/100)
        B=A-(C*100)
        D=math.trunc(B/10)
        U=B-(D*10)
        print(M,"M +",C,"C +",D,"D +",U,"U")
else:
    print("este numero tiene mas de 4 cifras")      