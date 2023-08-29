N=int(input("Introduzca un numero:"))

Miles=N//1000
Centenas=(N-(1000*Miles))//100
Decenas=(N-(1000*Miles)-(100*Centenas))//10
Unidades=((N-(1000*Miles)-(Centenas*100))-(Decenas*10))//1

De=N//10
Un=N-(10*De)//1

D=N//100
C=(N-(100*D))//10
U=(N-(100*D)-(10*C))//1


if N>999:
    print(Miles,"M","+",Centenas,"C","+",Decenas,"D","+",Unidades,"U")
if N<10:
    print(N,"U")
if N>=10 and N<=99:
    print(De,"D","+",U,"U")
if N>=100 and N<=999:
    print(D,"C","+",C,"D","+",U,"U")
