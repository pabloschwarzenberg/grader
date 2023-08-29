numero=int(input("ingrese un numero"))
Um=numero//1000
C=(numero-(Um*1000))//100
D=(numero-(Um*1000)-(C*100))//10
U=(numero-(Um*1000)-(C*100)-(D*10))//1
print(Um,"M +",C,"C +",D,"D +",U,"U")