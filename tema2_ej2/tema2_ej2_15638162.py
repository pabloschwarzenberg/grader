# completa el código de la función
def amigos(a,b):
    y=0
    i=1
    contador=1
    suma=0
    suma2=0
    x=0
    z=0
    w=0

    if a>b:
        
        while i<=b:
            if b%i==0:
                suma=suma+i
            else:
                pass   
            i=i+1

        if suma-b==a and suma2-a==b:
            x=True
        else:
            x=False

            

        while contador<=a:
            if a%contador==0:
                suma2=suma2+contador
            else:
                pass   
            contador+=1

        if suma2-a==b and suma-b==a:
            y=True
        else:
            y=False




    elif b>a:
        while i<=a:
            if a%i==0:
                suma=suma+i
            else:
                pass   
            i=i+1
        if suma-a==b and suma2-b==a:
            x=True
        else:
            x=False




        while contador<=b:
            if b%contador==0:
                suma2=suma2+contador
            else:
                pass   
            contador+=1

        if suma2-b==a and suma-a==b:
            y=True
        else:
            y=False
        



    elif a==b:
        while i<=b:
            if b%i==0:
                suma=suma+i
            else:
                pass   
            i=i+1

        if suma-b==a and suma2-a==b:
            z=True
        else:
            z=False

    elif a==1 or b==1:
        w=False
        

    if x==True or y==True or z==True:
        w=True
    else:
        w= False




    print(suma, suma2)

    return w 