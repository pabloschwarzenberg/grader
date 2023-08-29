def suma_divisores(a):
    a=int(a)
    numeros=0
    for i in range (1,a):
        if a%i==0:
            numeros+=i
    
    if a==1:
        return numeros,False
    if a<2:
        return numeros,False
    elif a==2:
        return numeros,True
    else:
        for i in range(2,a):
            if(a%i)==0:
                return numeros,False
            elif(i==a-1):
                return numeros,True
    



           

           