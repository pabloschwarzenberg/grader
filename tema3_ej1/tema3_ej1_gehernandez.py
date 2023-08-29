def suma_divisores(a):
    if a>1:
        i=1
        div=0
        while i<=(a):
            p=a%i
            if p==0:
                div=div+i
            div=div
            i=i+1
        if (div-a)==1:
            return (div-a,True)  
        return (div-a,False)
    else:
        return (0,False)