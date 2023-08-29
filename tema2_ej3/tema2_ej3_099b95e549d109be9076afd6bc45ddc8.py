def numero_perfecto(a):
    div=0
    tru=True
    for i in range(a):
        if a%(i+1)==0:
            div=div+(i+1)
    if a==1:
        tru=False
        return(tru)        
    elif (div-a)==a:
        tru=True
        return(tru)
    elif((div-a)!=a):
        tru=False
        return(tru)



