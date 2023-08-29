n=int(input("ingrese un numero de cuatro digitos= "))
if 0<n<10000:
    #unidad
    U=n%10
    n1=n//10
    #decenas
    D=n1%10
    n1=n1//10
    #centenas
    C=n1%10
    n1=n1//10
    #miles
    M=n1%10
#respuestas
    if 999<n<10000:
        print(M,"M +",C,"C +",D,"D +",U ,"U")
    elif 99<n<1000:
        print(C,"C + ",D,"D + ",U,"U")
    elif 9<n<100:
        print(D,"D + ",U,"U")
    elif 0<n<10:
        print(U,"U")