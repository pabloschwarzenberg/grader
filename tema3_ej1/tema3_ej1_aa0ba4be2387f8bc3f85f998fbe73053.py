# completa el código de la función
def suma_divisores(a):
    div=0
    tru=True
    for i in range(a):
        if a%(i+1)==0:
            div=div+(i+1)
    if a==1:
        tru=False
        return(div-a,tru)        
    elif (div-a)==1:
        tru=True
        return(div-a,tru)
    elif((div-a)!=1):
        tru=False
        return(div-a,tru)


