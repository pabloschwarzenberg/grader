def amigos(numero1,numero2):
    suma_divisores1=0
    suma_divisores2=0


    for i in range(1,numero1+1):
        if(numero1%i)==0:
            print(i)
            suma_divisores1=suma_divisores1+i
    for i in range(1,numero2+1):
        if(numero2%i)==0:
            print(i)
            suma_divisores2=suma_divisores2+i

    print(suma_divisores1,suma_divisores2)
    if (suma_divisores1==suma_divisores2) and (numero1!=numero2):
        return(True)
    else:
        return(False)
        
