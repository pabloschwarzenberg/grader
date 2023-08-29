T = int(input("Ingrese numero a descomponer :"))

Numero = str(T)
M = Numero[0:1]
C = Numero[1:2]
D = Numero[2:3]
U = Numero[3:4]
if (T >=1000):
    print(M,"M","+",C,"C","+",D,"D","+",U,"U")
elif (T<100):
    print(M,"D","+",C,"U","+")
elif(T>=100) and (T<1000):
    print(M,"C","+",C,"D","+",D,"U")