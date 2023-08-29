#Descomponer un número
num=int(input("Escribe un número con un máximo de 4 dígitos: "))
M=num//1000
C=(num-(M*1000))//100
D=(num-(M*1000)-(C*100))//10
U=(num-(M*1000)-(C*100)-(D*10))

if num>=1000 and num<=9999:
   print(M,"M +",C,"C +",D,"D +",U,"U")
elif num>=100 and num<=999:
   print(C,"C +",D,"D +",U,"U")
elif num>=10 and num<=99:
   print(D,"D +",U,"U")
elif num>=0 and num<=9:
   print(U,"U")
