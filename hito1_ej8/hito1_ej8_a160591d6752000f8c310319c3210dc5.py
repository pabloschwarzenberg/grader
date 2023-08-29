#Descomponer un número
num=int(input("Ingrese un número entero de hasta 4 dígitos: "))

if num>9999:
    print("Error. El número ingresado excede el límite de dígitos especificado.")
else:
    aux1=(num-num%1000)
    mil=aux1//1000
    aux2=(num-num%100)
    cen=(aux2-aux1)//100
    aux3=(num-num%10)
    dec=(aux3-aux2)//10
    uni=(num-aux3)

    if mil!=0:
        print(mil,"M + ",cen,"C + ",dec,"D + ",uni,"U")
    elif mil==0 and cen!=0:
        print(cen,"C + ",dec,"D + ",uni,"U")
    elif mil==0 and cen==0 and dec!=0:
        print(dec,"D + ",uni,"U")
    else:
        print(uni,"U")