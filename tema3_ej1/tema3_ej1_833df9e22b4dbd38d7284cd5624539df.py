def suma_divisores(numero):
        if numero==1:
            return(0,False)
        suma_divisores=0
        for i in range(2,numero):
                if(numero%i)==0:
                    suma_divisores=suma_divisores+i
           
        if suma_divisores>1 :
            suma_total=suma_divisores+1
            return(suma_total,False)
        else:
                return(1,True)


