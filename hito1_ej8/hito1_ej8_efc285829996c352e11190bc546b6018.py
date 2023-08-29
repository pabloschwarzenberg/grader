#Descomponer un número
numero=int(input("Ingrese un numero de hasta 4 digitos: "))
while not numero<9999 and numero>-9999:
    numero = int(input("Error, ingrese un numero de hasta 4 digitos: "))

largo=len(str(numero))
if largo==4:
    mil=numero//1000
    cent=(numero%1000)//100
    dec=(numero%100)//10
    uni=numero%10
    print(str(mil)+"M + "+str(cent)+"C + "+str(dec)+"D + "+str(uni)+"U")
elif largo==3:
    cent=(numero%1000)//100
    dec=(numero%100)//10
    uni=numero%10
    print(str(cent)+"C + "+str(dec)+"D + "+str(uni)+"U")
elif largo==2:
    dec=(numero%100)//10
    uni=numero%10
    print(str(dec)+"D + "+str(uni)+"U")
else:
    print(str(numero)+"U")     