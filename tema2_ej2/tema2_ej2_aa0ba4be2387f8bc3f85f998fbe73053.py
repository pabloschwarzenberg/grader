# completa el código de la función
def amigos(a,b):
    div=0
    tru=True
    for i in range(a):
        if a%(i+1)==0:
            div=div+(i+1)
    div1=0
    for j in range(b):
        if b%(j+1)==0:
            div1=div1+(j+1)

    if a==b:
        tru=False
        return(tru)     
    elif (div)==(div1):
        tru=True
        return(tru)
    else:
        tru=False
        return(tru)
           