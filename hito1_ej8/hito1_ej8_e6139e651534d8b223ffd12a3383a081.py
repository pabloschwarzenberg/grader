n=int(input("Escribe un numero"))
M=n//1000
C=int((n-(M*1000))//100)
D=int((n-(M*1000)-(C*100))//10)
U=int((n-(M*1000)-(C*100)-(D*10))//1)
print (M,"M","+",C,"C","+",D,"D","+",U,"U")
