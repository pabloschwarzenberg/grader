#Descomponer un número
print("SOLO PUEDES INGRESAR UN MÁXIMO DE 4 DIGITOS")
num=int(input("Dame el número que quieras descomponer:",))
nums=str(num)
largo=len(nums)

if largo==4:
    M=num//1000
    resto1=num%1000
    C=resto1//100
    resto2=resto1%100
    D=resto2//10
    resto3=resto2%10
    U=resto3//1
    resto4=resto3%1

    print("Tu número descompuesto es:",M,"M +",C,"C +",D,"D +",U,"U")

elif largo==3:
    C=num//100
    resto1=num%100
    D=resto1//10
    resto2=resto1%10
    U=resto2//1
    resto3=resto2%1

    print("Tu número descompuesto es:",C,"C +",D,"D +",U,"U")

elif largo==2:
    D=num//10
    resto1=num%10
    U=resto1//1
    resto2=resto1%1

    print("Tu número descompuesto es:",D,"D +",U,"U")

elif largo==1:
    U=num//1
    resto1=num%1

    print("Tu número descompuesto es:",U,"U")

else:
    print("Recuerde que su número solo puede ser un máximo de 4 digitos ")