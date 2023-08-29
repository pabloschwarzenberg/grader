numero = int (input ('Ingresa el valor de numero: '))
miles=(numero%10000-numero%1000)//1000
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10
M=repr (miles)+"M"
C=repr (centenas)+"C"
D=repr (decenas)+"D"
U=repr (unidades)+"U"



if miles>0:
    print(M,"+",C,"+",D,"+",U)
elif centenas >0:
    print(C,"+",D,"+",U)
elif decenas >0:
    print(D,"+",U)
elif unidades >0:
    print(U)