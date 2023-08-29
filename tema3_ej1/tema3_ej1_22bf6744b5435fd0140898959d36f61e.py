# completa el código de la función
def suma_divisores(a):

    x=int(a)
    i=1
    sumatoria=0

    while i>0:
        if (x%i)==0:
            if i==x:
                break
            
            sumatoria=sumatoria+i
            print(sumatoria)
            i=i+1
            continue

        else:
            i=i+1
            continue

    if sumatoria==1:
        return(sumatoria, True)
        
    elif x==1:
        return(sumatoria, False )

    else:
        return(sumatoria, False)
           