#Descomponer un número
n=eval(input("Numero:"))
if n<10:
    print(n,"U")
elif n>=10 and n<=99:
    U=n%10
    D=(n-U)//10
    print(D,"D +",U,"U")
elif n>=100 and n<999:
    U=n%10
    D=((n%100)-U)//10
    C=(n-U-D)//100
    print(C,"C +",D,"D +",U,"U")
elif n>=1000 and n<9999:
    U=n%10
    D=((n%100)-U)//10
    C=((n%1000)-D-U)//100
    M=(n-U-D-C)//1000
    print(M,"M +",C,"C +",D,"D +",U,"U")